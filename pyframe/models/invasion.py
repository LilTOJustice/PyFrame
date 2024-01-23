from collections import defaultdict
from models.common import Reward, WarframeObj
from dateutil.parser import isoparse

class AttackerDefender(WarframeObj):
    def __init__(self, json_attacker: dict):
        json_attacker = defaultdict(lambda : None, json_attacker)
        self.reward = Reward(json_attacker['reward']) if 'reward' in json_attacker else None
        self.faction = json_attacker['faction']
        self.faction_key = json_attacker['factionKey']

class Invasion(WarframeObj):
    def __init__(self, json_invasion: dict):
        json_invasion = defaultdict(lambda : None, json_invasion)
        self.id = json_invasion['id']
        self.activation = isoparse(json_invasion['activation']) if 'activation' in json_invasion else None
        self.expiry = isoparse(json_invasion['expiry']) if 'expiry' in json_invasion else None
        self.start_string = json_invasion['startString']
        self.active = json_invasion['active']
        self.attacker = AttackerDefender(json_invasion['attacker']) if 'attacker' in json_invasion else None
        self.attacker_reward = Reward(json_invasion['attackerReward']) if 'attackerReward' in json_invasion else None
        self.attacking_faction = json_invasion['attackingFaction']
        self.completed = json_invasion['completed']
        self.completion = json_invasion['completion'] if 'completion' in json_invasion else []
        self.count = json_invasion['count']
        self.defender = AttackerDefender(json_invasion['defender']) if 'defender' in json_invasion else None
        self.defender_reward = Reward(json_invasion['defenderReward']) if 'defenderReward' in json_invasion else None
        self.defending_faction = json_invasion['defendingFaction']
        self.desc = json_invasion['desc']
        self.eta = json_invasion['eta']
        self.node = json_invasion['node']
        self.node_key = json_invasion['nodeKey']
        self.required_runs = json_invasion['requiredRuns']
        self.reward_types = json_invasion['rewardTypes'] if 'rewardTypes' in json_invasion else []
        self.vs_infestation = json_invasion['vsInfestation']