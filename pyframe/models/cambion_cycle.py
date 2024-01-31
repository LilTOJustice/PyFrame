from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class CambionCycle(WarframeObj):
    def __init__(self, json_cambion_cycle: dict):
        self.id = str(json_cambion_cycle['id']) if 'id' in json_cambion_cycle else None
        self.expiry = isoparse(json_cambion_cycle['expiry']) if 'expiry' in json_cambion_cycle else None
        self.activation = isoparse(json_cambion_cycle['activation']) if 'activation' in json_cambion_cycle else None
        self.state = str(json_cambion_cycle['state']) if 'state' in json_cambion_cycle else None
        self.active = bool(json_cambion_cycle['active']) if 'active' in json_cambion_cycle else None
        self.time_left = str(json_cambion_cycle['timeLeft']) if 'timeLeft' in json_cambion_cycle else None