import falcon

from rapinator.model.text_model import StaticModel
from rapinator.resources.song import SongResource

api = falcon.API()

song = SongResource(StaticModel())
api.add_route('/song', song)
