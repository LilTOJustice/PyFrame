from collections import defaultdict
from dateutil.parser import isoparse
from pyframe.models.common import WarframeObj
    
class Arbitration(WarframeObj):
    def __init__(self, json_arbitration: dict):
        json_arbitration = defaultdict(lambda : None, json_arbitration)
        self.id = json_arbitration['id']
        self.activation = isoparse(json_arbitration['activation']) if 'activation' in json_arbitration else None
        self.expiry = isoparse(json_arbitration['expiry']) if 'expiry' in json_arbitration else None
        self.start_string = json_arbitration['startString']
        self.active = json_arbitration['active']
        self.node = json_arbitration['node']
        self.enemy = json_arbitration['enemy']
        self.enemy_key = json_arbitration['enemyKey']
        self.type = json_arbitration['type']
        self.type_key = json_arbitration['typeKey']
        self.archwing = json_arbitration['archwing']
        self.sharkwing = json_arbitration['sharkwing']