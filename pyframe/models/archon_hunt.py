from collections import defaultdict
from dateutil.parser import isoparse
from pyframe.models.common import WarframeObj, Mission

class ArchonHunt(WarframeObj):
    def __init__(self, json_archon_hunt: dict):
        json_archon_hunt = defaultdict(lambda : None, json_archon_hunt)
        self.id = json_archon_hunt['id']
        self.activation = isoparse(json_archon_hunt['activation'])
        self.expiry = isoparse(json_archon_hunt['expiry'])
        self.start_string = json_archon_hunt['startString']
        self.active = json_archon_hunt['active']
        self.reward_pool = json_archon_hunt['rewardPool']
        self.missions = [Mission(mission) for mission in json_archon_hunt['missions']] if 'missions' in json_archon_hunt else []
        self.boss = json_archon_hunt['boss']
        self.faction = json_archon_hunt['faction']
        self.faction_key = json_archon_hunt['factionKey']
        self.expired = json_archon_hunt['expired']
        self.eta = json_archon_hunt['eta']