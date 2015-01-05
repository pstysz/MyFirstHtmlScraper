# -*- coding: utf-8 -*-
import re
import time
from models.digger import Category

def speed_test():
    selected_data = Category.select(Category.name).tuples()
    test_data = ['historia', 'wojna', 'swiat', 'rzym', 'piec', 'auto', 'krakow', 'rok', 'b;uwefb', 'historia', 'swiat', 'zydzi', 'jedzenie', 'zus', '3rb34']
    found_data = None
    #1
    start_time = time.time()
    for item in test_data:
        found_data = item in selected_data
    print('1. {0}'.format(time.time() - start_time))

    #2
    start_time = time.time()
    for item in test_data:
        try:
            found_data = Category.get(Category.name == item).name
        except:
            pass
    print('2. {0}'.format(time.time() - start_time))