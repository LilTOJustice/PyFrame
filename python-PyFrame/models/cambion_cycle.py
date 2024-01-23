from collections import defaultdict
from models.common import WarframeObj
from dateutil.parser import isoparse

class CambionCycle(WarframeObj):
    def __init__(self, json_cambion_cycle: dict):
        json_cambion_cycle = defaultdict(lambda : None, json_cambion_cycle)
        self.id = json_cambion_cycle['id']
        self.expiry = isoparse(json_cambion_cycle['expiry']) if 'expiry' in json_cambion_cycle else None
        self.activation = isoparse(json_cambion_cycle['activation']) if 'activation' in json_cambion_cycle else None
        self.state = json_cambion_cycle['state']
        self.active = json_cambion_cycle['active']
        self.time_left = json_cambion_cycle['timeLeft']