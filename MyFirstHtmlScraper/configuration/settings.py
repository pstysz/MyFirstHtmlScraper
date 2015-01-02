# -*- coding: utf-8 -*-
import logging

'''DO NOT INCLUDE THIS FILE TO SOURCE CONTROL!!!'''

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

DBSETTINGS = {
    'mysql': {
        'database': 'content_generators',
        'user': 'pstysz',
        'passwd': 'pspsps',
        'host': 'localhost',
        'port': 3306
    },
    'sqlite3':{
        'database': 'test.db'
    }
}

KICKER_ROOT_URL = 'http://www.wykop.pl/wykopalisko/'

KICKER_SUBSITE_PATTERN = KICKER_ROOT_URL + 'strona/{{site_number}}/' #{{site_number}} is taken from last site number