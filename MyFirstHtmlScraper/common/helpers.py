# -*- coding: utf-8 -*-
import logging
import bs4
import requests
import re
from unidecode import unidecode
from models.shared import SOURCE_TYPE

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

def get_tag_from_string(input_string):
    '''Creates tag from input string, that means:
       1. Removes all non alphanumeric characters
       2. Removes diacritics
       3. Return lowered string '''
    alphanum_str = re.sub(r'[^\w+]','', input_string)
    return unidecode(alphanum_str.lower())

def remove_html_from_string(input_string):
    return re.sub('<[^<]+?>', '', input_string)


def get_content_from_article(source, source_id):
    '''Extract and save to db content from article.
       Returns True for success and False if fail'''
    if source == SOURCE_TYPE['unknown']:
        pass
    elif source == SOURCE_TYPE['pclab']:
        pass
    return False

def create_content():
    '''Scan db for unextracted articles and create content from them'''
    #TODO: Call get_content_from_article here
    pass

