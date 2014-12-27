# Search functionality for Seek

from BeautifulSoup import BeautifulSoup
import requests
import urllib

def search_engine(term, result=0):
    # TODO: Get engine preference from config.
    return search_duckduckgo(term, result)

# This doesn't work yet
def search_google(term, result=0):
    result = requests.get("https://www.google.com/#q=" + urllib.quote_plus(term))

def search_duckduckgo(term, result=0):
    search_result = requests.get('https://duckduckgo.com/html/?q=' + urllib.quote_plus(term))
    soup = BeautifulSoup(search_result.content)
   
    # Skip ads. Sorry DDG.
    ad_offset = 2
    link = soup.findAll('a', rel='nofollow')[ad_offset + result]
    link_url = link['href']

    return link_url
