# -*- coding: utf-8 -*-
import configuration.settings
import logging
import time
from models.orm import initiate_db
from scrapers import digger, pclab
from common import helpers

from tests.test import speed_test

if __name__ == '__main__':
    initiate_db()
    start_time = time.time()
    digger.start_scraping()
    pclab.start_scraping() 
    logging.info('Finish, scraping took {0}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))))