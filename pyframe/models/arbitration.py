from pyframe.models.common import WarframeObj, isoparse
    
class Arbitration(WarframeObj):
    def __init__(self, json_arbitration: dict):
        self.id = str(json_arbitration['id'])
        self.activation = isoparse(json_arbitration['activation']) if 'activation' in json_arbitration else None
        self.expiry = isoparse(json_arbitration['expiry']) if 'expiry' in json_arbitration else None
        self.start_string = str(json_arbitration['startString']) if 'startString' in json_arbitration else None
        self.active = bool(json_arbitration['active']) if 'active' in json_arbitration else None
        self.node = str(json_arbitration['node']) if 'node' in json_arbitration else None
        self.enemy = str(json_arbitration['enemy']) if 'enemy' in json_arbitration else None
        self.enemy_key = str(json_arbitration['enemyKey']) if 'enemyKey' in json_arbitration else None
        self.type = str(json_arbitration['type']) if 'type' in json_arbitration else None
        self.type_key = str(json_arbitration['typeKey']) if 'typeKey' in json_arbitration else None
        self.archwing = bool(json_arbitration['archwing']) if 'archwing' in json_arbitration else None
        self.sharkwing = bool(json_arbitration['sharkwing']) if 'sharkwing' in json_arbitration else None