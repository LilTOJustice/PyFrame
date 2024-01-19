from models.common import WarframeObj
from collections import defaultdict
from dateutil.parser import isoparse

class Incursions(WarframeObj):
    def __init__(self, json_incursions: dict):
        json_incursions = defaultdict(lambda : None, json_incursions)
        self.id = json_incursions['id']
        self.activation = isoparse(json_incursions['activation']) if 'activation' in json_incursions else None
        self.expiry = isoparse(json_incursions['expiry']) if 'expiry' in json_incursions else None
        self.active = json_incursions['active']

class SteelPathItem(WarframeObj): 
    def __init__(self, json_steel_path_item: dict):
        json_steel_path_item = defaultdict(lambda : None, json_steel_path_item)
        self.name = json_steel_path_item['name']
        self.cost = json_steel_path_item['cost']

class SteelPath(WarframeObj):
    def __init__(self, json_steel_path: dict):
        json_steel_path = defaultdict(lambda : None, json_steel_path)
        self.activation = isoparse(json_steel_path['activation']) if 'activation' in json_steel_path else None
        self.expiry = isoparse(json_steel_path['expiry']) if 'expiry' in json_steel_path else None
        self.current_reward = SteelPathItem(json_steel_path['currentReward']) if 'currentReward' in json_steel_path else None
        self.remaining = json_steel_path['remaining']
        self.rotation = [SteelPathItem(rotation) for rotation in json_steel_path['rotation']] if 'rotation' in json_steel_path else []
        self.evergreens = [SteelPathItem(evergreen) for evergreen in json_steel_path['evergreens']] if 'evergreens' in json_steel_path else []
        self.incursions = Incursions(json_steel_path['incursions']) if 'incursions' in json_steel_path else None