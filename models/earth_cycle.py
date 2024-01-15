from models.common import WarframeObj
from collections import defaultdict
from dateutil.parser import isoparse

class EarthCycle(WarframeObj):
    def __init__(self, json_earth_cycle: dict):
        json_earth_cycle = defaultdict(lambda : None, json_earth_cycle)
        self.id = json_earth_cycle['id']
        self.activation = isoparse(json_earth_cycle['activation']) if 'activation' in json_earth_cycle else None
        self.expiration = isoparse(json_earth_cycle['expiry']) if 'expiry' in json_earth_cycle else None
        self.start_string = json_earth_cycle['startString']
        self.active = json_earth_cycle['active']
        self.is_day = json_earth_cycle['isDay']
        self.time_left = json_earth_cycle['timeLeft']