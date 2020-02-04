import requests

artist = 'Yung Lean'
response = requests.get(f'http://localhost:8000/song?{artist}')
print(response)