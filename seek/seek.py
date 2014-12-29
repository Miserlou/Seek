#! /usr/bin/env python

import requests
import urllib
import argparse

from pyglance import glance
from search import search_engine

# Really shouldn't do this.
DIFFBOT_API_TOKEN = '2efef432c72b5a923408e04353c39a7c'

def get_page_data(url):
    diffbot_url = 'http://api.diffbot.com/v2/article?url=' + urllib.quote_plus(url) + "&token=" + DIFFBOT_API_TOKEN
    page = requests.get(diffbot_url)
    data = page.json()

    if 'error' in data:
        print data['error']
        quit()

    return data

def extract_data(url):
    from goose import Goose
    g = Goose()
    article = g.extract(url)

    data = {} 
    data['title'] = article.title
    data['url'] = article.canonical_link
    data['text'] = article.cleaned_text
    
    return data

def print_body(data):
    
    if 'text'  in data:
        print data['text']
        print ""
        print data['title']
        print data['url'] 
    else:
        print "No usable text found."

def glance_body(data, speed=600):
    print data['title']
    print data['url'] 
    glance(data['text'], speed)

def get_parser():
    parser = argparse.ArgumentParser(description='Command line searching for incredibly lazy people.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
            help='the question to answer')
    parser.add_argument('-p','--pos', help='select answer in specified position (default: 0)', default=0, type=int)
    parser.add_argument('-t','--text', help='display answer as plaintext', default=True, dest='plaintext', action='store_true')
    parser.add_argument('-g','--glance', help='display result in glance format', default=False, dest='glancemode', action='store_true')
    parser.add_argument('-s','--speed', help='WPM to glance at.', default=600, dest='speed', type=int)
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['query']:
        parser.print_help()
        return
    else:
        seek(args)

def seek(args):
    term = ' '.join(args['query']).replace('?', '') 
    link_url = search_engine(term, args['pos'])
    #data = get_page_data(link_url)
    data = extract_data(link_url)
    if args['glancemode']:
        glance_body(data, args['speed'])
    else:
        print_body(data)

if __name__ == '__main__':
    command_line_runner()
