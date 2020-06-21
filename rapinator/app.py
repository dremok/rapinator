import falcon

from rapinator.model.transformer_model import GPT2
from rapinator.resources.song import SongResource

api = falcon.API()

song = SongResource(GPT2())
api.add_route('/song', song)
