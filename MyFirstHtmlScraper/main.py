# -*- coding: utf-8 -*-
import configuration.settings
import logging
import time
from models.orm import initiate_db
from scrapers import digger, pclab


if __name__ == '__main__':
    start_time = time.time()
    initiate_db()
    digger.start_scraping()
    #start_scraping_pclab()
    #digger.scrap_site('http://www.wykop.pl/wykopalisko/strona/1/')

    logging.info('Scraping took {0}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))))