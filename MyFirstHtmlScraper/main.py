# -*- coding: utf-8 -*-
import logging
import time
from scrapers import digger, pclab
from models.shared import initiate_db

if __name__ == '__main__':
    start_time = time.time()
    initiate_db()
    #start_scraping_digger()
    #start_scraping_pclab()
    digger.scrap_site('http://www.wykop.pl/wykopalisko/strona/9/')

    logging.info('Scraping took {0}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))))