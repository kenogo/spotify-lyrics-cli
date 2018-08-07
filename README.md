# spotify-lyrics-cli

This is a simple python script to automatically scrape www.genius.com lyrics based on the currently playing Spotify song (using the Linux native Spotify client). Actually, other media players than Spotify can be used as long as they use the DBus MediaPlayer2 interface. An example would be VLC. There program can also fetch lyrics for mpd.

The program can be used by downloading and extracting the zip and simply running.

```
python lyrics.py [spotify|vlc|...]
```

## Dependencies

Needs the python libraries `bs4`, `lxml` and `requests`. And, obviously, Spotify :)

If you want to fetch lyrics for mpd, you'll also need the python library `mpd`.
