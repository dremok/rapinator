import json

import falcon

from rapinator.model.lyrics_generator import LyricsGenerator


class SongResource:
    def __init__(self):
        self.generator = LyricsGenerator()

    def on_get(self, req, resp):
        artist = req.query_string
        raw_lyrics = self.generator.sample_model(f'<<{artist} - ')
        title, lyrics = self.generator.parse_lyrics(raw_lyrics)
        song = {
            'artist': artist,
            'title': title,
            'lyrics': lyrics,
        }
        resp.body = json.dumps(song, ensure_ascii=False)
        resp.status = falcon.HTTP_200
