from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class Fissure(WarframeObj):
    def __init__(self, json_fissure: dict):
        self.id = str(json_fissure['id']) if 'id' in json_fissure else None
        self.activation = isoparse(json_fissure['activation']) if 'activation' in json_fissure else None 
        self.expiry = isoparse(json_fissure['expiry']) if 'expiry' in json_fissure else None 
        self.start_string = str(json_fissure['startString']) if 'startString' in json_fissure else None
        self.active = bool(json_fissure['active']) if 'active' in json_fissure else None
        self.node = str(json_fissure['node']) if 'node' in json_fissure else None
        self.expired = str(json_fissure['expired']) if 'expired' in json_fissure else None
        self.eta = str(json_fissure['eta']) if 'eta' in json_fissure else None
        self.mission_type = str(json_fissure['missonType']) if 'missionType' in json_fissure else None
        self.mission_key = str(json_fissure['missionKey']) if 'missionKey' in json_fissure else None
        self.tier = str(json_fissure['tier']) if 'tier' in json_fissure else None
        self.tier_num = int(json_fissure['tierNum']) if 'tierNum' in json_fissure else None
        self.enemy = str(json_fissure['enemy']) if 'enemy' in json_fissure else None
        self.enemy_key = str(json_fissure['enemyKey']) if 'enemyKey' in json_fissure else None
        self.is_storm = bool(json_fissure['isStorm']) if 'isStorm' in json_fissure else None
        self.is_hard = bool(json_fissure['isHard']) if 'isHard' in json_fissure else None
