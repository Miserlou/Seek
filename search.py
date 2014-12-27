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
  
    # Skip the ads. Sorry DDG.
    # There is probably a better way to do this using a better selector rather than looping. TODO.
    divs = soup.findAll('div', 'results_links')
    for div in divs:
        if 'web-result-sponsored' in div['class']:
            divs.remove(div)

    link = divs[result]
    link_url = link.findAll('a')[0]['href']

    return link_url
