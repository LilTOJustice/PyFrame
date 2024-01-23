from collections import defaultdict
from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class Kuva(WarframeObj):
    def __init__(self, json_kuva: dict):
        json_kuva = defaultdict(lambda : None, json_kuva)
        self.id = json_kuva['id']
        self.activation = isoparse(json_kuva['activation']) if 'activation' in json_kuva else None
        self.expiry = isoparse(json_kuva['expiry']) if 'expiry' in json_kuva else None
        self.start_string = json_kuva['startString']
        self.active = json_kuva['active']
        self.node = json_kuva['node']
        self.enemy = json_kuva['enemy']
        self.enemy_key = json_kuva['enemyKey']
        self.type = json_kuva['type']
        self.type_key = json_kuva['typeKey']
        self.archwing = json_kuva['archwing']
        self.sharkwing = json_kuva['sharkwing']