
import requests
import logging
import bs4
from multiprocessing import pool
import re
import sys
from app.models import Post

def get_soup_for_url(url):
    try:
        logging.info('Getting response for {0}...'.format(url))
        response = requests.get(url)
        logging.info('Generating soup for {0}...'.format(url))
        soup = bs4.BeautifulSoup(response.text)
        return soup
    except requests.exceptions.RequestException as e: 
        print(e)
        sys.exit(1)


def get_last_site_number(soup):
    try:
        #gets last site number from footer
        logging.info('Getting last site number')
        page_number = soup.select('div.pager > p > a')[-2].get_text()
        return int(page_number)
    except:  
        #TODO: Implement some nice exception handling
        raise 

def get_links_from_soup(soup):
    try:
        #gets links for all subsites in soup
        logging.info('Getting links for subsites')
        return [link.attrs.get('href') for link in soup.select('div.article div.lcontrast h2 a')]
    except:  
        #TODO: Implement some nice exception handling
        raise 

def get_posts_from_soup(soup):
    try:
        #gets links for all subsites in soup
        logging.info('Getting posts from soup')
        posts = []
        for p in soup.select('div.article'):
            post = Post()
            post.id = p.attrs.get('data-id')
            #FIXME: lcontrast is a list, not a soup
            lcontrast = p.select('div.lcontrast')
            post.title = lcontrast.select('h2 a')[0].get_text()
            post.url = lcontrast.select('h2 a')[0].attrs.get('href')
            post.description = lcontrast.select('div.description p a')[0].get_text()
            posts.append(post)

        return posts
    except:  
        #TODO: Implement some nice exception handling
        raise 


# EXAMPLES

#def get_video_page_urls(index_url):
#    logging.info('Getting requests.response...')
#    response = requests.get(index_url)
#    logging.info('Getting soup...')
#    soup = bs4.BeautifulSoup(response.text)
#    logging.info('Getting links...')
#    return [('http://pyvideo.org' + a.attrs.get('href')) for a in soup.select('div.video-summary-data a[href^=/video]')]

#def get_video_data(video_page_url):
#    video_data = {}
#    response = requests.get(video_page_url)
#    soup = bs4.BeautifulSoup(response.text)
#    video_data['title'] = soup.select('div#videobox h3')[0].get_text()
#    video_data['speakers'] = [a.get_text() for a in soup.select('div#sidebar a[href^=/speaker]')]
 
#    # initialize counters
#    video_data['views'] = 0
#    video_data['likes'] = 0
#    video_data['dislikes'] = 0
 
#    try:
#        video_data['youtube_url'] = soup.select('div#sidebar a[href^=http://www.youtube.com]')[0].get_text()
#        response = requests.get(video_data['youtube_url'], headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'})
#        soup = bs4.BeautifulSoup(response.text)
#        video_data['views'] = int(re.sub('[^0-9]', '', soup.select('.watch-view-count')[0].get_text().split()[0]))
#        video_data['likes'] = int(re.sub('[^0-9]', '', soup.select('#watch-like-dislike-buttons span.yt-uix-button-content')[0].get_text().split()[0]))
#        video_data['dislikes'] = int(re.sub('[^0-9]', '', soup.select('#watch-like-dislike-buttons span.yt-uix-button-content')[2].get_text().split()[0]))
#    except:
#        # some or all of the counters could not be scraped
#        pass
#    return video_data

#def show_video_stats(index_url):
#    video_page_urls = get_video_page_urls(index_url)
#    for video_page_url in video_page_urls:
#        print(get_video_data(video_page_url))