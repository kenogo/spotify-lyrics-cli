# spotify-lyrics-cli

This is a simple bash script combined with a python script to automatically scrape www.musixmatch.com lyrics based on the currently playing Spotify song (using the Linux native Spotify client). The bash script is used for getting the Spotify song info, the python script is used for web scraping. This means other bash scripts could easily be written to include other players then Spotify. This can be used by downloading and extracting the zip and simply running.

```
chmod +x getlyrics
./getlyrics
```
Credits for the bash script go to [this thread](https://gist.github.com/febuiles/1549991)

## Dependencies

Needs the python libraries `bs4` and `request`. And, obviously, Spotify :)
