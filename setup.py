from setuptools import setup

setup(name="spotify-lyrics-cli",
      version="0.1",
      description="Automatically fetch lyrics from spotify and other music"
                  " players",
      url="https://github.com/kenogo/spotify-lyrics-cli",
      author="Keno Goertz",
      author_email="keno@goertz-berlin.com",
      packages=["spotify_lyrics_cli"],
      scripts=["bin/lyrics-cli"],
      install_requires=["beautifulsoup4", "requests", "lxml"],
      zip_safe=False)
