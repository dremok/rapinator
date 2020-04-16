import os

from definitions import ROOT_DIR
from rapinator.model.lyrics_generator import LyricsGenerator
from rapinator.model.null_model import NullModel


class TestLyricsGenerator:
    def test_parse_lyrics(self):
        raw_lyrics = '''<<Kanye West - Â Adolescent Witchcraft>>
        
        
        
[Intro]

(It's not too late for us to make it. The message's clear

Some music that is going to really make a little sense of why we're having fun




Some'''

        os.chdir(ROOT_DIR)

        generator = LyricsGenerator(NullModel())
        parsed = generator.parse_lyrics(raw_lyrics)
        assert parsed[0] == 'Â Adolescent Witchcraft'
        assert parsed[1].startswith('[Intro]')
        assert parsed[1].endswith("we're having fun")
