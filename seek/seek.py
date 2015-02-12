#! /usr/bin/env python

import requests
import urllib
import argparse

from pyglance import glance, get_page_data
from search import search_engine

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
        try:
            seek(args)
        except (KeyboardInterrupt, SystemExit):
            print "" 
            quit()
        except Exception, e:
            quit()

def seek(args):
    term = ' '.join(args['query']).replace('?', '') 
    link_url = search_engine(term, args['pos'])
    data = get_page_data(link_url)
    if args['glancemode']:
        glance_body(data, args['speed'])
    else:
        print_body(data)

if __name__ == '__main__':
    try:
        command_line_runner()
    except (KeyboardInterrupt, SystemExit):
        print "" 
        quit()
    except Exception, e:
        quit()
