from pyframe.models.common import WarframeObj, isoparse

class Variant(WarframeObj):
    def __init__(self, json_variant: dict):
        self.node = str(json_variant['node']) if 'node' in json_variant else None
        self.boss = str(json_variant['boss']) if 'boss' in json_variant else None
        self.mission_type = str(json_variant['missionType']) if 'missionType' in json_variant else None
        self.planet = str(json_variant['planet']) if 'planet' in json_variant else None
        self.modifier = str(json_variant['modifier']) if 'modifier' in json_variant else None
        self.modifier_description = str(json_variant['modifierDescription']) if 'modifierDescription' in json_variant else None

class Sortie(WarframeObj):
    def __init__(self, json_sortie: dict):
        self.id = str(json_sortie['id']) if 'id' in json_sortie else None
        self.activation = isoparse(json_sortie['activation']) if 'activation' in json_sortie else None
        self.expiry = isoparse(json_sortie['expiry']) if 'expiry' in json_sortie else None
        self.start_string = str(json_sortie['startString']) if 'startString' in json_sortie else None
        self.active = bool(json_sortie['active']) if 'active' in json_sortie else None
        self.reward_pool = str(json_sortie['rewardPool']) if 'rewardPool' in json_sortie else None
        self.variants = [Variant(variant) for variant in json_sortie['variants']] if 'variants' in json_sortie else None
        self.boss = str(json_sortie['boss']) if 'boss' in json_sortie else None
        self.faction = str(json_sortie['faction']) if 'faction' in json_sortie else None
        self.faction_key = str(json_sortie['factionKey']) if 'factionKey' in json_sortie else None
        self.expired = bool(json_sortie['expired']) if 'expired' in json_sortie else None
        self.eta = str(json_sortie['eta']) if 'eta' in json_sortie else None