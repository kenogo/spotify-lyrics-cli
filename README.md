# spotify-lyrics-cli

This is a simple bash script combined with a python script to automatically scrape www.genius.com (and if that fails, www.musixmatch.com) lyrics based on the currently playing Spotify song (using the Linux native Spotify client). Actually, other media players than Spotify can be used as long as they use the DBus MediaPlayer2 interface. An example would be VLC.

The bash script is used for getting the Spotify song info with a dbus message, the python script is used for web scraping. This means other bash scripts could easily be written to include other players that don't support the MediaPlayer2 interface but might have some other way to obtain song info.

The program can be used by downloading and extracting the zip and simply running.

```
chmod +x getlyrics
./getlyrics [spotify|vlc|...]
```
Credits for the bash script go to [this thread](https://gist.github.com/febuiles/1549991)

## Dependencies

Needs the python libraries `bs4`, `lxml` and `requests`. And, obviously, Spotify :)
