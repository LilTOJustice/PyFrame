from pyframe.models.common import WarframeObj, isoparse

class Incursions(WarframeObj):
    def __init__(self, json_incursions: dict):
        self.id = str(json_incursions['id']) if 'id' in json_incursions else None
        self.activation = isoparse(json_incursions['activation']) if 'activation' in json_incursions else None
        self.expiry = isoparse(json_incursions['expiry']) if 'expiry' in json_incursions else None
        self.active = bool(json_incursions['active']) if 'active' in json_incursions else None

class SteelPathItem(WarframeObj): 
    def __init__(self, json_steel_path_item: dict):
        self.name = str(json_steel_path_item['name']) if 'name' in json_steel_path_item else None
        self.cost = int(json_steel_path_item['cost']) if 'cost' in json_steel_path_item else None

class SteelPath(WarframeObj):
    def __init__(self, json_steel_path: dict):
        self.activation = isoparse(json_steel_path['activation']) if 'activation' in json_steel_path else None
        self.expiry = isoparse(json_steel_path['expiry']) if 'expiry' in json_steel_path else None
        self.current_reward = SteelPathItem(json_steel_path['currentReward']) if 'currentReward' in json_steel_path else None
        self.remaining = str(json_steel_path['remaining']) if 'remaining' in json_steel_path else None
        self.rotation = [SteelPathItem(rotation) for rotation in json_steel_path['rotation']] if 'rotation' in json_steel_path else []
        self.evergreens = [SteelPathItem(evergreen) for evergreen in json_steel_path['evergreens']] if 'evergreens' in json_steel_path else []
        self.incursions = Incursions(json_steel_path['incursions']) if 'incursions' in json_steel_path else None