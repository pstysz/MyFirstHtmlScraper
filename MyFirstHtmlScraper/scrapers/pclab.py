﻿# -*- coding: utf-8 -*-
import logging
import multiprocessing
import re
from models.shared import Category, SourceArticle, SourceArticleToCategory, Content, SOURCE_TYPE
from dateutil.parser import parse
from common.helpers import get_urls_from_pattern, get_soup_for_url, get_tag_from_string, remove_html_from_string
from configuration.settings import PCLAB_SITE_PATTERN, PCLAB_ARTICLE_PATTERN, DB_HANDLER


def start_scraping():
    first_site = get_urls_from_pattern(1, PCLAB_SITE_PATTERN)[0]
    base_soup = get_soup_for_url(first_site)
    no_of_sites = get_last_site_number(base_soup)
    url_list = get_urls_from_pattern(no_of_sites, PCLAB_SITE_PATTERN)

    # debug
    existing_ids = SourceArticle.select(SourceArticle.source_id).where(SourceArticle.source_type == SOURCE_TYPE['pclab'])
    test_id = 61250
    test_val = test_id in existing_ids
    for t in existing_ids:
        print(t.source_id)

    # wrong method
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

def get_art_urls_from_news_list(news_url, existing_ids):
    '''Returns urls to articles from passed url to list of articles.
       Result is list of urls to new articles (not added to db yet)'''
    articles_urls = []

    for url in url_list:
        soup = get_soup_for_url(url)
        ids = [int(re.findall(r'\d+', a.attrs.get('href'))[0]) for a in soup.select('div.list div.element div.title a')]
        for id in ids:
            try:
                if SourceArticle.select().where((SourceArticle.source == SOURCE_TYPE['pclab']) & (SourceArticle.source_id == id)).count():
                    continue
            except:
                pass
        debug = existing_ids
        #TODO: Filter urls by existing ids, add only new
    return articles_urls

def create_article_from_url(article_url):
    '''Save article from passed url to database if not already exists
       Returns True for success and False if article already exists'''
    article_id = int(re.findall(r'\d+', article_url)[0])
    if not SourceArticle.select().where((SourceArticle.source_type == SOURCE_TYPE['pclab']) & (SourceArticle.source_id == article_id)).exists():
        soup = get_soup_for_url(article_url)
        paragraphs = [remove_html_from_string(p.get_text()) for p in soup.select('div.main div.substance div.data p')]
        while '' in paragraphs:
            paragraphs.remove('')
        text = ' '.join(paragraphs)
        article = SourceArticle.create(text=text, source_type=SOURCE_TYPE['pclab'], source_id=article_id)
        tags = [get_tag_from_string(a.get_text()) for a in soup.select('div.main div.substance div.tags a')]
        sourcearticle_to_category = []
        for tag in tags:
            new_category = None
            try:
                new_category = Category.get(Category.name == tag)
                new_category.popularity_pclab += 1
                new_category.save()      
            except Category.DoesNotExist:
                new_category = Category.create(name=tag, popularity_pclab=1) 
            except:
                raise
            sourcearticle_to_category.append({'source_article': article.id, 'category': new_category.id})
        with DB_HANDLER.transaction():
            for idx in range(0, len(sourcearticle_to_category), 1000): # bulk insert in 1000 pcs chunks
                SourceArticleToCategory.insert_many(sourcearticle_to_category[idx:idx+1000]).execute()
        return True
    return False