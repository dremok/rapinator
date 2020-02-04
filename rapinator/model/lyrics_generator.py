import json
import re

import numpy as np
import tensorflow as tf

from rapinator import utils
from rapinator.model import encoder
from rapinator.model import model
from rapinator.model import sample


class LyricsGenerator:
    def __init__(self,
                 model_name='345M',
                 seed=None,
                 batch_size=1,
                 length=None,
                 temperature=1,
                 top_k=0,
                 top_p=0.0):
        self.enc = encoder.get_encoder(model_name)
        hparams = model.default_hparams()
        with open(str(utils.get_project_root() / 'models' / model_name / 'hparams.json')) as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx // 2
        elif length > hparams.n_ctx:
            raise ValueError(f"Can't get samples longer than window size: {hparams.n_ctx}")

        self.sess = tf.Session()
        self.context = tf.placeholder(tf.int32, [batch_size, None])
        np.random.seed(seed)
        tf.set_random_seed(seed)
        self.output = sample.sample_sequence(
            hparams=hparams, length=length,
            context=self.context,
            batch_size=batch_size,
            temperature=temperature, top_k=top_k, top_p=top_p
        )

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(utils.get_project_root() / 'models' / model_name)
        saver.restore(self.sess, ckpt)

    def sample_model(
            self,
            model_input,
            batch_size=1
    ):
        context_tokens = self.enc.encode(model_input)
        out = self.sess.run(self.output, feed_dict={
            self.context: [context_tokens for _ in range(batch_size)]
        })[:, len(context_tokens):]
        text = ''
        for i in range(batch_size):
            text += self.enc.decode(out[i])
        return text

    def parse_lyrics(self, raw_lyrics):
        m = re.search('<<.+? - (.+?)>>', raw_lyrics)
        try:
            title = m.group(1)
        except Exception:
            title = 'Untitled'
        whitelist = set('$1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \n')
        return title, ''.join(filter(whitelist.__contains__, raw_lyrics))
