# -*- coding: utf-8 -*-
import logging
import django
import time
from digger_functions import start_scraping_digger

#region Configuration

#TODO: Add logging to file
#eg: logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
django.setup()

#endregion Configuration


if __name__ == '__main__':
    start_time = time.time()
    start_scraping_digger()
    logging.info('Scraping took {0}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))))