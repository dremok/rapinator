import re


class LyricsGenerator:
    def __init__(self, model):
        self.model = model

    def sample_model(self, model_input: str) -> str:
        return self.model.sample(model_input)

    def parse_lyrics(self, raw_lyrics):
        m = re.search('<<.+? - (.+?)>>', raw_lyrics)
        try:
            title = m.group(1).strip()
        except Exception:
            title = 'Untitled'
        whitelist = set("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' \n[]()$.,:&")
        lyrics = raw_lyrics[:raw_lyrics.rfind('***')].replace('*', '')
        lyrics = lyrics[lyrics.index('\n') + 1:lyrics.rfind('\n')]
        lyrics = re.sub(r'\n\n', '\n', lyrics).strip()
        lyrics = re.sub(r'[^\n]\n\[', '\n\n[', lyrics)
        return title, ''.join(filter(whitelist.__contains__, lyrics))
