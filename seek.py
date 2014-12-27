#! /usr/bin/env python

from clint import arguments
import requests
import urllib
import argparse

from search import search_engine

# Really shouldn't do this.
DIFFBOT_API_TOKEN = '2efef432c72b5a923408e04353c39a7c'

def get_page_body(url):
    diffbot_url = 'http://api.diffbot.com/v2/article?url=' + urllib.quote_plus(url) + "&token=" + DIFFBOT_API_TOKEN
    page = requests.get(diffbot_url)
    data = page.json()

    if 'error' in data:
        print data['error']
        quit()
    if 'text'  in data:
        print data['text']
        print ""
        print data['title']
        print url
    else:
        print "No usable text found."

def get_parser():
    parser = argparse.ArgumentParser(description='Command line searching for incredibly lazy people.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
            help='the question to answer')
    parser.add_argument('-p','--pos', help='select answer in specified position (default: 0)', default=0, type=int)
    parser.add_argument('-l','--link', help='display only the answer link',
            action='store_true')
    parser.add_argument('-t','--text', help='display answer as plaintext', default=True, type=bool)
    parser.add_argument('-g','--glance', help='display result in glance format at this WPM (default 800).', default=800, type=int)
    parser.add_argument('-v','--version', help='displays the current version of seek',
            action='store_true')
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if args['version']:
        print(__version__)
        return
    if not args['query']:
        parser.print_help()
        return
    else:
        seek(args)

def seek(args):
    term = ' '.join(args['query']).replace('?', '') 
    link_url = search_engine(term, args['pos'])
    get_page_body(link_url)

if __name__ == '__main__':
    command_line_runner()
