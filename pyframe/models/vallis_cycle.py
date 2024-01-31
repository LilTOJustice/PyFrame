from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class VallisCycle(WarframeObj):
    def __init__(self, json_vallis_cycle : dict):
        self.id = str(json_vallis_cycle['id']) if 'id' in json_vallis_cycle else None
        self.expiry = isoparse(json_vallis_cycle['expiry']) if 'expiry' in json_vallis_cycle else None
        self.time_left = str(json_vallis_cycle['timeLeft']) if 'timeLeft' in json_vallis_cycle else None
        self.is_warm = bool(json_vallis_cycle['isWarm']) if 'isWarm' in json_vallis_cycle else None
