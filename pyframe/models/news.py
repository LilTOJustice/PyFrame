from pyframe.models.common import WarframeObj, isoparse

class News(WarframeObj):
    def __init__(self, json_news: dict):
        self.date = isoparse(json_news['date']) if 'date' in json_news else None
        self.image_link = str(json_news['imageLink']) if 'imageLink' in json_news else None
        self.eta = str(json_news['eta']) if 'eta' in json_news else None
        self.prime_access = bool(json_news['primeAcess']) if 'primeAcess' in json_news else None
        self.stream = bool(json_news['stream']) if 'stream' in json_news else None
        self.translations = Translation(json_news['translations']) if 'translations' in json_news else None
        self.link = str(json_news['link']) if 'link' in json_news else None
        self.update = bool(json_news['update']) if 'update' in json_news else None
        self.id = str(json_news['id']) if 'id' in json_news else None
        self.as_string = str(json_news['asString']) if 'asString' in json_news else None
        self.message = str(json_news['message']) if 'message' in json_news else None
        self.priority = bool(json_news['priority']) if 'priority' in json_news else None

class Translation(WarframeObj):
    def __init__(self, json_translation: dict):
        self.es = str(json_translation['es']) if 'es' in json_translation else None
