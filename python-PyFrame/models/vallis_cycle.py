from collections import defaultdict
from models.common import WarframeObj
from dateutil.parser import isoparse

class VallisCycle(WarframeObj):
    def __init__(self, json_vallis_cycle : dict):
        json_vallis_cycle = defaultdict(lambda : None, json_vallis_cycle)
        self.id = json_vallis_cycle['id']
        self.expiry = isoparse(json_vallis_cycle['expiry']) if 'expiry' in json_vallis_cycle else None
        self.time_left = json_vallis_cycle['timeLeft']
        self.is_warm = json_vallis_cycle['isWarm']
