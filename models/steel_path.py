from models.common import WarframeObj
from collections import defaultdict
from dateutil.parser import isoparse

class SteelPath(WarframeObj):
    def __init__(self, json_steel_path: dict):
        json_steel_path = defaultdict(lambda : None, json_steel_path)
        self.activation = isoparse(json_steel_path['activation']) if 'activation' in json_steel_path else None
        self.expiry = isoparse(json_steel_path['expiry']) if 'expiry' in json_steel_path else None
        self.current_reward = CurrentReward(json_steel_path['current_reward']) if 'current_reward' in json_steel_path else None
        self.remaining = json_steel_path['remaining']
        self.rotation = Rotation(json_steel_path['rotation'])
        self.evergreens = json_steel_path['evergreens']
        self.incursions = Incursions(json_steel_path['incursions']) if 'incursions' in json_steel_path else None

class CurrentReward(WarframeObj):
    def __init__(self, json_current_reward: dict):
        json_current_reward = defaultdict(lambda : None, json_current_reward)
        self.name = json_current_reward['name']
        self.cost = json_current_reward['cost']

class Incursions(WarframeObj):
    def __init__(self, json_incursions: dict):
        json_incursions = defaultdict(lambda : None, json_incursions)
        self.id = json_incursions['id']
        self.activation = isoparse(json_incursions['activation']) if 'activation' in json_incursions else None
        self.expiry = isoparse(json_incursions['expiry']) if 'expiry' in json_incursions else None
        self.active = json_incursions['active']

class Rotation(WarframeObj):
    def __init__(self, json_rotation: dict):
        json_rotation = defaultdict(lambda : None, json_rotation)
        self.name = json_rotation['name']
        self.cost = json_rotation['cost']