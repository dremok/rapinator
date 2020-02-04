import falcon

from rapinator.resources.song import SongResource

api = application = falcon.API()

song = SongResource()
api.add_route('/song', song)
