import json

import requests

artist = 'Kanye West'
response = requests.get(f'http://localhost:8000/song?artist={artist}')
song_dict = json.loads(response.content.decode('UTF-8'))
print(song_dict['lyrics'])
