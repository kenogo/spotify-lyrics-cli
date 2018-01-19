import requests
import sys
from bs4 import BeautifulSoup
import os

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus


def get_lyrics(song_name):

    song_name += ' musixmatch'
    name = quote_plus(song_name)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'
           '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    url = 'http://www.google.com/search?q=' + name

    result = requests.get(url, headers=hdr).text
    link_start = result.find('https://www.musixmatch.com')

    if(link_start == -1):
        return("Lyrics not found on musixmatch")
        
    link_end = result.find('"', link_start + 1)
    link = result[link_start:link_end]

    lyrics_html = requests.get(link, headers={
                               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel'
                               'Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, '
                               'like Gecko) Chrome/55.0.2883.95 Safari/537.36'
                               }
                               ).text

    soup = BeautifulSoup(lyrics_html, "lxml")
    lyrics = str(soup.findAll('p', attrs={'class': 'mxm-lyrics__content'}))
    lyrics = lyrics[1:len(lyrics)-1]
    lyrics = lyrics.replace('<p class="mxm-lyrics__content ">', '')
    lyrics = lyrics.replace('</p>', '')
    return lyrics

print(sys.argv[2].upper()+' - '+sys.argv[1].upper()+'\n')
print(get_lyrics(sys.argv[1]+' '+sys.argv[2]))
