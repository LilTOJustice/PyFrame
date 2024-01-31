from pyframe.models.common import WarframeObj, Mission, isoparse

class ArchonHunt(WarframeObj):
    def __init__(self, json_archon_hunt: dict):
        self.id = str(json_archon_hunt['id']) if 'id' in json_archon_hunt else None
        self.activation = isoparse(json_archon_hunt['activation']) if 'activation' in json_archon_hunt else None
        self.expiry = isoparse(json_archon_hunt['expiry']) if 'expiry' in json_archon_hunt else None
        self.start_string = str(json_archon_hunt['startString']) if 'startString' in json_archon_hunt else None
        self.active = bool(json_archon_hunt['active']) if 'active' in json_archon_hunt else None
        self.reward_pool = str(json_archon_hunt['rewardPool']) if 'rewardPool' in json_archon_hunt else None
        self.missions = [Mission(mission) for mission in json_archon_hunt['missions']] if 'missions' in json_archon_hunt else []
        self.boss = str(json_archon_hunt['boss']) if 'boss' in json_archon_hunt else None
        self.faction = str(json_archon_hunt['faction']) if 'faction' in json_archon_hunt else None
        self.faction_key = str(json_archon_hunt['factionKey']) if 'factionKey' in json_archon_hunt else None
        self.expired = bool(json_archon_hunt['expired']) if 'expired' in json_archon_hunt else None
        self.eta = str(json_archon_hunt['eta']) if 'eta' in json_archon_hunt else None