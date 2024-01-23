from collections import defaultdict
from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class Variant(WarframeObj):
    def __init__(self, json_variant: dict):
        json_variant = defaultdict(lambda : None, json_variant)
        self.node = json_variant['node']
        self.boss = json_variant['boss']
        self.mission_type = json_variant['missionType']
        self.planet = json_variant['planet']
        self.modifier = json_variant['modifier']
        self.modifier_description = json_variant['modifierDescription']

class Sortie(WarframeObj):
    def __init__(self, json_sortie: dict):
        json_sortie = defaultdict(lambda : None, json_sortie)
        self.id = json_sortie['id']
        self.activation = isoparse(json_sortie['activation']) if 'activation' in json_sortie else None
        self.expiry = isoparse(json_sortie['expiry']) if 'expiry' in json_sortie else None
        self.start_string = json_sortie['startString']
        self.active = json_sortie['active']
        self.reward_pool = json_sortie['rewardPool']
        self.variants = [Variant(variant) for variant in json_sortie['variants']] if 'variants' in json_sortie else None
        self.boss = json_sortie['boss']
        self.faction = json_sortie['faction']
        self.faction_key = json_sortie['factionKey']
        self.expired = json_sortie['expired']
        self.eta = json_sortie['eta']