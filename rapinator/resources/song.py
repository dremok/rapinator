import json

import falcon

from rapinator.model.lyrics_generator import LyricsGenerator


class SongResource:
    def __init__(self):
        self.generator = LyricsGenerator()

    def on_get(self, req, resp):
        print(req.query_string)
        print(falcon.uri.parse_query_string(req.query_string))
        artist = falcon.uri.parse_query_string(req.query_string)['artist']
        print(f'Generating lyrics for "{artist}"')
        raw_lyrics = self.generator.sample_model(f'<<{artist} - ')
        print(raw_lyrics)
        title, lyrics = self.generator.parse_lyrics(raw_lyrics)
        song = {
            'artist': artist,
            'title': title,
            'lyrics': lyrics,
        }
        resp.body = json.dumps(song, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        resp.body = json.dumps({'test'}, ensure_ascii=False)
        resp.status = falcon.HTTP_200
