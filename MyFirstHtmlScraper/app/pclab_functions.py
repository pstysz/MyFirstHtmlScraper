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
from global_functions import get_urls_from_pattern, get_soup_for_url


SITE_PATTERN =  'http://pclab.pl/news-{{site_number}}-100.html' #{{site_number}} is taken from last site number
ARTICLE_PATTERN = 'http://pclab.pl/news{{article_id}}.html'

def start_scraping_pclab():
    first_site = get_urls_from_pattern(1, SITE_PATTERN)[0]
    base_soup = get_soup_for_url(first_site)
    no_of_sites = get_last_site_number(base_soup)
    url_list = get_urls_from_pattern(no_of_sites, SITE_PATTERN)
    articles_urls =  get_art_urls_from_list(url_list)
    no_of_pools = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(no_of_pools)
    #pool.map_async(scrap_site, urls)
    #pool.close()
    #pool.join()

def get_last_site_number(soup):
    try:
        #gets last site number from footer
        logging.info('Getting last site number')
        page_number = soup.select('div.pages div.offset a')[-2].get_text()
        return int(page_number)
    except:  
        #TODO: Implement some nice exception handling
        raise 

def scrap_site(url):
    try:
        logging.info('Start scapring {0}'.format(url))
        soup = get_soup_for_url(url)
       # create_posts_from_soup(soup)
    except:
        #TODO: Implement some nice exception handling
        raise

def get_art_urls_from_list(url_list):
    '''returns urls to articles from passed url to list of articles'''
    articles_urls = []
    existing_ids = Post.objects.only('id')
    for url in url_list:
        soup = get_soup_for_url(url)
        ids = [int(re.findall(r'\d+', a.attrs.get('href'))[0]) for a in soup.select('div.list div.element div.title a')]
        existing_ids.append(*ids)
        debug = existing_ids
        #TODO: Filter urls by existing ids, add only new
    return articles_urls
