﻿# -*- coding: utf-8 -*-
import logging
import multiprocessing
import re
from models.shared import Category #, SourceArticle, SourceArticleToCategory, Content
from dateutil.parser import parse
from common.helpers import get_urls_from_pattern, get_soup_for_url
from configuration.settings import PCLAB_SITE_PATTERN, PCLAB_ARTICLE_PATTERN


def start_scraping():
    first_site = get_urls_from_pattern(1, PCLAB_SITE_PATTERN)[0]
    base_soup = get_soup_for_url(first_site)
    no_of_sites = get_last_site_number(base_soup)
    url_list = get_urls_from_pattern(no_of_sites, PCLAB_SITE_PATTERN)
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
