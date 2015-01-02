# -*- coding: utf-8 -*-
import requests
import logging
import bs4
import multiprocessing
import re
import sys
import os
sys.path.append('../orm/')
sys.path.append('.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")
from app.models import Post, Category
from dateutil.parser import parse
from global_functions import get_urls_from_pattern

ROOT_URL = 'http://www.wykop.pl/wykopalisko/'
SITE_PATTERN = ROOT_URL + 'strona/{{site_number}}/' #{{site_number}} is taken from last site number

def start_scraping_digger():
    base_soup = get_soup_for_url(ROOT_URL)
    no_of_sites = get_last_site_number(base_soup)
    urls = get_urls_from_pattern(no_of_sites, SITE_PATTERN)
    no_of_pools = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(no_of_pools)
    pool.map_async(scrap_site, urls)
    pool.close()
    pool.join()

def get_soup_for_url(url):
    try:
        logging.info('Getting response for {0}'.format(url))
        response = requests.get(url)
        logging.info('Generating soup for {0}'.format(url))
        soup = bs4.BeautifulSoup(response.text, "lxml")
        return soup
    except requests.exceptions.RequestException as e: 
        print(e)
        sys.exit(1)

def get_last_site_number(soup):
    try:
        #gets last site number from footer
        logging.info('Getting last site number')
        page_number = soup.select('div.pager > p > a')[-2].get_text()
        return int(page_number)
    except:  
        #TODO: Implement some nice exception handling
        raise 

def create_posts_from_soup(soup):
    try:
        #gets links for all subsites in soup
        logging.info('Getting posts from soup')
        posts = []

        for article in soup.select('ul#itemsStream div.article'):
            temp_desc = article.select('div.lcontrast div.description p a')[0].get_text().strip()
            if len(temp_desc) < 100:
                continue #get only posts with text longer than 100 chars

            temp_id = article.attrs.get('data-id')
            logging.info('Getting posts id = {0}'.format(temp_id))
            temp_popularity = article.select('div.diggbox span')[0].get_text().strip()
            if (not temp_popularity.isdigit()) or (temp_id is None):
                continue #popularity is not number for ad posts
            temp_popularity = int(temp_popularity)

            #check if post already exist in db and update popularity or insert new post
            if Post.objects.filter(pk=temp_id).exists():
                #post with selected id already exists == only update popularity
                post = Post.objects.get(pk=temp_id)
                if post.popularity != temp_popularity:
                    post.popularity = temp_popularity
                    logging.info('Updating posts id = {0}'.format(temp_id))
                    post.save()
            else:
                #post with selected id doesnt exist yet == create new post
                post = Post()
                post.id = temp_id
                post.popularity = temp_popularity
                post.title = article.select('div.lcontrast h2 a')[0].get_text().strip()
                post.url = article.select('div.lcontrast h2 a')[0].attrs.get('href').strip()
                post.description = article.select('div.lcontrast div.description p a')[0].get_text().strip()
                post.image_url = article.select('div.media-content img')[0].attrs.get('data-original')
                if post.image_url is None:
                    post.image_url = article.select('div.media-content img')[0].attrs.get('src')
                post.date = parse(article.select('div.lcontrast div.row span.affect time')[0].attrs.get('datetime'))

                tags = [a.attrs.get('href').split('/')[-2] for a in article.select('a.tag') if not a.attrs.get('href') is None]
                categories = []
                for tag in tags:
                    (new_category, isCreated) = Category.objects.get_or_create(name=tag)
                    new_category.popularity += 1
                    new_category.appears_on_digger = True
                    new_category.save()
                    categories.append(new_category)
                if len(categories) > 0:
                    # add many-to-many relation between created post and categories
                    logging.info('Creating posts id = {0}'.format(temp_id))
                    post.save()
                    post.category.add(*categories)
                    logging.info('Adding {0} categories posts id = {1}'.format(len(categories), temp_id))
                    post.save()
                else:
                    posts.append(post)   
        if len(posts) > 0:
            logging.info('Bulk create {0} posts'.format(len(posts)))
            Post.objects.bulk_create(posts) #insert on database if not saved before

    except:  
        #TODO: Implement some nice exception handling
        raise 

def scrap_site(url):
    try:
        logging.info('Start scapring {0}'.format(url))
        soup = get_soup_for_url(url)
        create_posts_from_soup(soup)
    except:
        #TODO: Implement some nice exception handling
        raise