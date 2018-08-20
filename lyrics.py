import argparse
from bs4 import BeautifulSoup
import dbus
import re
import requests
import sys

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

def get_lyrics_genius(artist, title):
    title = re.sub(r"\(.*\)|\[.*\]", '', title) # (feat.) [extended cut]
    title = re.sub(r"-.*", '', title) # - Remastered ...
    # Google for Lyrics
    search_name = "%s %s genius lyrics" % (artist, title)
    name = quote_plus(search_name)
    url = 'http://www.google.com/search?q=' + name
    result = requests.get(url).text
    link_start = result.find('https://genius.com')
    if(link_start == -1):
        return "Lyrics could not be found..."
    link_end = result.find('"', link_start + 1)
    link = result[link_start:link_end].lower()
    link = re.sub(r"&.*", '', link) # Remove PHP nonesense
    link_correct = check_link_genius(artist, title, link)
    if not link_correct:
        return "Lyrics could not be found..."

    # Get the lyrics from genius
    lyrics_html = requests.get(link).text
    soup = BeautifulSoup(lyrics_html, "lxml")
    raw_lyrics = str(soup.findAll('div', attrs={'class': 'lyrics'}))
    lyrics = raw_lyrics[1:len(raw_lyrics)-1]
    lyrics = re.sub(r"<[^<>]*>", '', lyrics) # Remove HTML tags
    if sys.version_info < (3, 0):
        lyrics = re.sub(r"\\n", '\n', lyrics)
    lyrics = lyrics[2:] # Remove two newlines
    return lyrics

def check_link_genius(artist, title, link):
    songinfo = "%s %s" % (artist, title)
    songinfo = songinfo.lower()
    songinfo = re.sub(r"[^a-zA-Z0-9 ]", '', songinfo) # Remove special chars
    songinfo_array = songinfo.split()
    for item in songinfo_array:
        if link.find(item) == -1:
            return False
    return True

def get_song_info(player):
    if player == "mpd":
        from mpd import MPDClient
        client = MPDClient()
        client.connect("localhost", 6600)
        song_info = client.currentsong()
        return song_info["artist"], song_info["title"]
    else:
        bus = dbus.SessionBus()
        try:
            proxy = bus.get_object("org.mpris.MediaPlayer2.%s" % player,
                                   "/org/mpris/MediaPlayer2")
        except dbus.exceptions.DBusException:
            print("[ERROR] Player \"%s\" doesn't exist or isn't playing" \
                  % player)
            return

        interface = dbus.Interface(
            proxy, dbus_interface="org.freedesktop.DBus.Properties"
        )
        properties = interface.GetAll("org.mpris.MediaPlayer2.Player")
        metadata = properties["Metadata"]
        artist = str(metadata["xesam:artist"][0])
        title = str(metadata["xesam:title"])
        return artist, title

def main():
    parser = argparse.ArgumentParser(description="Display lyrics automatically")
    parser.add_argument("player", type=str, help="e.g. spotify,vlc,...")
    args = parser.parse_args()
    artist, title = get_song_info(args.player)
    print("%s - %s\n" % (artist.upper(), title.upper()))
    print(get_lyrics_genius(artist, title))

if __name__ == "__main__":
    main()
