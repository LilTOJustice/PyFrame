from models.common import WarframeObj
from collections import defaultdict
from dateutil.parser import isoparse
from models.common import WarframeObj

class CetusCycle(WarframeObj):
    def __init__(self, json_cetus_cycle: dict):
        json_cetus_cycle = defaultdict(lambda : None, json_cetus_cycle)
        self.id = json_cetus_cycle['id']
        self.activation = isoparse(json_cetus_cycle['activation']) if 'activation' in json_cetus_cycle else None
        self.expiry = isoparse(json_cetus_cycle['expiry']) if 'expiry' in json_cetus_cycle else None
        self.start_string = json_cetus_cycle['startString']
        self.active = json_cetus_cycle['active']
        self.is_day = json_cetus_cycle['isDay']
        self.state = json_cetus_cycle['state']
        self.time_left = json_cetus_cycle['timeLeft']
        self.is_cetus = json_cetus_cycle['isCetus']
        self.short_string = json_cetus_cycle['shortString']
