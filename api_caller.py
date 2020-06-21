import json

import requests

artist = 'Eminem'

response = requests.get(f'http://localhost:8003/song?artist={artist}')
song_dict = json.loads(response.content.decode('UTF-8'))

song_title = song_dict['title']
lyrics = song_dict['lyrics']

print(f'Artist: {artist}')
print(f'Song: {song_title}')
print('\n\n')
print(lyrics)
