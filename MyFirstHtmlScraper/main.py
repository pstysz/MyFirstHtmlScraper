# -*- coding: utf-8 -*-
import logging
import time
from scrapers import digger, pclab
from peewee_models import initiate_db
# for debug
from digger import scrap_site

if __name__ == '__main__':
    start_time = time.time()
    initiate_db()
    #start_scraping_digger()
    #start_scraping_pclab()
    scrap_site('http://www.wykop.pl/wykopalisko/strona/9/')

    logging.info('Scraping took {0}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))))