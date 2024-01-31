from pyframe.models.common import WarframeObj, isoparse

class Kuva(WarframeObj):
    def __init__(self, json_kuva: dict):
        self.id = str(json_kuva['id']) if 'id' in json_kuva else None
        self.activation = isoparse(json_kuva['activation']) if 'activation' in json_kuva else None
        self.expiry = isoparse(json_kuva['expiry']) if 'expiry' in json_kuva else None
        self.start_string = str(json_kuva['startString']) if 'startString' in json_kuva else None
        self.active = bool(json_kuva['active']) if 'active' in json_kuva else None
        self.node = str(json_kuva['node']) if 'node' in json_kuva else None
        self.enemy = str(json_kuva['enemy']) if 'enemy' in json_kuva else None
        self.enemy_key = str(json_kuva['enemyKey']) if 'enemyKey' in json_kuva else None
        self.type = str(json_kuva['type']) if 'type' in json_kuva else None
        self.type_key = str(json_kuva['typeKey']) if 'typeKey' in json_kuva else None
        self.archwing = bool(json_kuva['archwing']) if 'archwing' in json_kuva else None
        self.sharkwing = bool(json_kuva['sharkwing']) if 'sharkwing' in json_kuva else None