# -*- coding: utf-8 -*-
import requests
import logging
import bs4
from multiprocessing import pool
import re
import sys
from app.models import Post, Category
from dateutil.parser import parse

def get_soup_for_url(url):
    try:
        logging.info('Getting response for {0}...'.format(url))
        response = requests.get(url)
        logging.info('Generating soup for {0}...'.format(url))
        soup = bs4.BeautifulSoup(response.text, "html5lib")
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

def get_links_from_soup(soup):
    try:
        #gets links for all subsites in soup
        logging.info('Getting links for subsites')
        return [link.attrs.get('href') for link in soup.select('div.article div.lcontrast h2 a')]
    except:  
        #TODO: Implement some nice exception handling
        raise 

def create_posts_from_soup(soup):
    try:
        #gets links for all subsites in soup
        logging.info('Getting posts from soup')
        posts = []

        for article in soup.select('ul#itemsStream div.article'):
            temp_id = article.attrs.get('data-id')
            logging.info('Getting posts id = {0}'.format(temp_id))
            temp_popularity = article.select('div.diggbox span')[0].get_text().strip()

            if (not temp_popularity.isdigit()) or (temp_id is None):
                continue # popularity is not number for ad posts

            temp_popularity = int(temp_popularity)

            #check if post already exist in db and update popularity or insert new post
            if Post.objects.filter(pk=temp_id).exists():
                #post with selected id already exists == only update popularity
                post = Post.objects.get(pk=temp_id)

                if post.popularity != temp_popularity:
                    post.popularity = temp_popularity
                    post.save()
            else:
                #post with selected id doesnt exist yet == create new post
                post = Post()
                post.id = temp_id
                post.popularity = temp_popularity
                post.title = article.select('div.lcontrast h2 a')[0].get_text().strip()
                post.url = article.select('div.lcontrast h2 a')[0].attrs.get('href').strip()
                post.description = article.select('div.lcontrast div.description p a')[0].get_text().strip()
                post.image_url = article.select('div.media-content img')[0].attrs.get('src')
                post.date = parse(article.select('div.lcontrast div.row span.affect time')[0].attrs.get('datetime'))
                tags = [a.attrs.get('href').split('/')[-2] for a in article.select('a.tag') if not a.attrs.get('href') is None]
                categories = []

                for tag in tags:
                    (new_category, isCreated) = Category.objects.get_or_create(name=tag)
                    categories.append(new_category)

                if len(categories) > 0:
                    # add many-to-many relation between created post and categories
                    post.save()
                    post.category.add(*categories)
                posts.append(post)
        
        if len(posts) > 0:
            Post.objects.bulk_create(posts) #insert on database

    except:  
        #TODO: Implement some nice exception handling
        raise 