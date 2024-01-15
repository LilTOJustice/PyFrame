from models.common import WarframeObj
from collections import defaultdict
from dateutil.parser import isoparse

class Fissure(WarframeObj):
    def __init__(self, json_fissure: dict):
        json_fissure = defaultdict(lambda : None, json_fissure)
        self.id = json_fissure['id']
        self.activation = isoparse(json_fissure['activation']) if 'activation' in json_fissure else None 
        self.expiry = isoparse(json_fissure['expiry']) if 'expiry' in json_fissure else None 
        self.start_string = json_fissure['startString']
        self.active = json_fissure['active']
        self.node = json_fissure['node']
        self.expired = json_fissure['expired']
        self.eta = json_fissure['eta']
        self.mission_type = json_fissure['missonType']
        self.mission_key = json_fissure['missionKey']
        self.tier = json_fissure['tier']
        self.tier_num = json_fissure['tierNum']
        self.enemy = json_fissure['enemy']
        self.enemy_key = json_fissure['enemyKey']
        self.is_storm = json_fissure['isStorm']
        self.is_hard = json_fissure['isHard']
