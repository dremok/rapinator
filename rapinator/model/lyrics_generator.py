import re

import gpt_2_simple as gpt2


class LyricsGenerator:
    def __init__(self):
        self.sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.sess)
        print('Done!')

    def sample_model(self, model_input):
        return gpt2.generate(self.sess, temperature=0.9, top_k=70, prefix=model_input, return_as_list=True)[0]

    def parse_lyrics(self, raw_lyrics):
        m = re.search('<<.+? - (.+?)>>', raw_lyrics)
        try:
            title = m.group(1)
        except Exception:
            title = 'Untitled'
        whitelist = set('[]()$1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \n')
        return title, ''.join(filter(whitelist.__contains__, raw_lyrics))
