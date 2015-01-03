# -*- coding: utf-8 -*-
import logging
import multiprocessing
from datetime import datetime
from models.shared import Category
from models.digger import KickerPost, KickerPostToCategory
from dateutil.parser import parse
from common.helpers import get_urls_from_pattern, get_soup_for_url
from configuration.settings import KICKER_ROOT_URL, KICKER_SUBSITE_PATTERN, DB_HANDLER

def start_scraping():
    base_soup = get_soup_for_url(KICKER_ROOT_URL)
    no_of_sites = get_last_site_number(base_soup)
    urls = get_urls_from_pattern(no_of_sites, KICKER_SUBSITE_PATTERN)
    no_of_pools = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(no_of_pools)
    pool.map_async(scrap_site, urls)
    pool.close()
    pool.join()

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
        kickerpost_to_category = []  # holds data for many-to-many table to bulk update at the end
        for article in soup.select('ul#itemsStream div.article'):
            temp_desc = article.select('div.lcontrast div.description p a')[0].get_text().strip()
            if len(temp_desc) < 100:
                continue #get only posts with text longer than 100 chars
            temp_id = article.attrs.get('data-id')
            logging.info('Getting post id = {0}'.format(temp_id))
            temp_popularity = article.select('div.diggbox span')[0].get_text().strip()
            if (not temp_popularity.isdigit()) or (temp_id is None):
                continue #popularity is not number for ad posts
            temp_popularity = int(temp_popularity)

            try:
                # if post with selected id already exists, only update popularity
                post = KickerPost.get(KickerPost.id == temp_id)           
                if post.popularity != temp_popularity:
                    post.popularity = temp_popularity
                    logging.info('Updating post id = {0}'.format(temp_id))
                    post.save()
            except KickerPost.DoesNotExist as e:
                #post with selected id doesnt exist yet == create new post
                logging.info('Creating post id = {0}'.format(temp_id))
                post = KickerPost.create(id=temp_id, description=temp_desc, popularity=temp_popularity)
                post.title = article.select('div.lcontrast h2 a')[0].get_text().strip()
                post.url = article.select('div.lcontrast h2 a')[0].attrs.get('href').strip()
                post.image_url = article.select('div.media-content img')[0].attrs.get('data-original')
                if post.image_url is None:
                    post.image_url = article.select('div.media-content img')[0].attrs.get('src')
                unparsed_date = article.select('div.lcontrast div.row span.affect time')[0].attrs.get('datetime')
                post.date = parse(unparsed_date, ignoretz=True)
                post.save()

                tags = [a.attrs.get('href').split('/')[-2] for a in article.select('a.tag') if not a.attrs.get('href') is None]
                for tag in tags:
                    new_category = None
                    try:
                        new_category = Category.get(Category.name == tag)
                        new_category.popularity_kicker += 1
                        new_category.save()      
                    except:
                        new_category = Category.create(name=tag, popularity_kicker=1) 
                    kickerpost_to_category.append({'post': post.id, 'category': new_category.id})
        with DB_HANDLER.transaction():
            for idx in range(0, len(kickerpost_to_category), 1000): # bulk insert in 1000 pcs chunks
                KickerPostToCategory.insert_many(kickerpost_to_category[idx:idx+1000]).execute()

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