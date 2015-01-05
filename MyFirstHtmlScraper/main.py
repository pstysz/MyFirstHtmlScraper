# -*- coding: utf-8 -*-
import configuration.settings
import logging
import time
from models.orm import initiate_db
from scrapers import digger, pclab

from tests.test import speed_test

if __name__ == '__main__':
    initiate_db()
    start_time = time.time()
    #digger.start_scraping()
    #pclab.start_scraping() 
    test_art = 'http://pclab.pl/news61250.html'
    pclab.create_article_from_url(test_art)

    logging.info('Scraping took {0}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))))