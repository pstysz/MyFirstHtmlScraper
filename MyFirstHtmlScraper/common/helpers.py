# -*- coding: utf-8 -*-
import logging
import bs4
import requests

def get_key_words_from_text(input_string, no_of_key_words):
    ''' Returns most common words from passed string'''
    logging.info('Pulling out {0} keywords from passed string '.format(no_of_key_words))
    cleared_string = [word[:-1] for word in re.sub(r'[^\w ]|[\d]', '', input_string).lower().split(' ') if len(word[:-2]) > 2]
    appearances = {}
    for word in cleared_string:
        if word in appearances:
            appearances[word] += 1
        else:
            appearances[word] = 1
    if no_of_key_words > 0:
        return sorted(appearances, key=appearances.get, reverse=True)[:no_of_key_words]
    return []

def get_urls_from_pattern(no_of_sites, site_pattern):
    return [site_pattern.replace('{{site_number}}', str(site_number)) for site_number in range(1, no_of_sites + 1)]

def get_soup_for_url(url):
    try:
        logging.info('Getting response for {0}'.format(url))
        response = requests.get(url)
        logging.info('Generating soup for {0}'.format(url))
        soup = bs4.BeautifulSoup(response.text, "lxml")
        return soup
    except requests.exceptions.RequestException as e: 
        print(e)
        sys.exit(1)