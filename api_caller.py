import json

import requests

artist = 'Yung Lean'
response = requests.get(f'http://localhost:8000/song?{artist}')
song_dict = json.loads(response.content.decode('UTF-8'))
print(song_dict['lyrics'])
