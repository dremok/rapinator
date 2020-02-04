import concurrent.futures
import sys

from rapinator.data.genius import Genius
from rapinator.data.genius import get_all_rappers


def download_artist(artist_name):
    try:
        genius.scrape_artist(artist_name, max_songs=50)
    except Exception:
        # TODO: Fix exception handling for HTTP errors
        pass


genius = Genius(sys.argv[1])
rappers = get_all_rappers()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download_artist, rappers)
