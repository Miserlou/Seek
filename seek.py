#! /usr/bin/env python

from clint import arguments
import requests
import urllib

from search import search_engine

# Really shouldn't do this.
DIFFBOT_API_TOKEN = '2efef432c72b5a923408e04353c39a7c'

def get_page_body(url):
    diffbot_url = 'http://api.diffbot.com/v2/article?url=' + urllib.quote_plus(url) + "&token=" + DIFFBOT_API_TOKEN
    page = requests.get(diffbot_url)
    data = page.json()

    if hasattr(data, 'error'):
        print data['error']
        quit()
    else:
        print data['text']


args = arguments.Args()
term = args[0]
link_url = search_engine(term)
get_page_body(link_url)
