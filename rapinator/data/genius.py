import os
from pathlib import Path

import lyricsgenius

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent


def get_all_rappers():
    rappers = []
    with open(Path(ROOT_DIR, 'data', 'rappers.txt')) as f:
        for rapper in [line.strip() for line in f.readlines()]:
            if '[' in rapper:
                rappers.append(rapper[:rapper.index('[')])
            else:
                rappers.append(rapper)
    return sorted(list(set(rappers)))


class Genius:
    def __init__(self, client_access_token):
        self._api = lyricsgenius.Genius(client_access_token)

    def scrape_artist(self, artist_name: str, max_songs=20):
        artist = self._api.search_artist(artist_name, max_songs)
        artist_path = Path(Path(ROOT_DIR), 'data', artist.name)
        os.makedirs(artist_path, exist_ok=True)
        for song in artist.songs:
            with open(Path(artist_path, f'{song.title}.txt'), 'w') as f:
                f.write(song.lyrics)
