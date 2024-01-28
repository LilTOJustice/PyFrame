from collections import defaultdict
from dateutil.parser import isoparse
from pyframe.models.common import WarframeObj

class News(WarframeObj):
    def __init__(self, json_news: dict):
        json_news = defaultdict(lambda : None, json_news)
        self.date = isoparse(json_news['date']) if 'date' in json_news else None
        self.image_link = json_news['imageLink']
        self.eta = json_news['eta']
        self.prime_access = json_news['primeAcess']
        self.stream = json_news['stream']
        self.translations = Translation(json_news['translations']) if 'translations' in json_news else None
        self.link = json_news['link']
        self.update = json_news['update']
        self.id = json_news['id']
        self.as_string = json_news['asString']
        self.message = json_news['message']
        self.priority = json_news['priority']

class Translation(WarframeObj):
    def __init__(self, json_translation: dict):
        json_translation = defaultdict(lambda : None, json_translation)
        self.es = json_translation['es']
