from pyframe.models.common import Reward, WarframeObj, isoparse

class AttackerDefender(WarframeObj):
    def __init__(self, json_attacker: dict):
        self.reward = Reward(json_attacker['reward']) if 'reward' in json_attacker else None
        self.faction = str(json_attacker['faction']) if 'faction' in json_attacker else None
        self.faction_key = str(json_attacker['factionKey']) if 'factionKey' in json_attacker else None

class Invasion(WarframeObj):
    def __init__(self, json_invasion: dict):
        self.id = str(json_invasion['id']) if 'id' in json_invasion else None
        self.activation = isoparse(json_invasion['activation']) if 'activation' in json_invasion else None
        self.expiry = isoparse(json_invasion['expiry']) if 'expiry' in json_invasion else None
        self.start_string = str(json_invasion['startString']) if 'startString' in json_invasion else None
        self.active = bool(json_invasion['active']) if 'active' in json_invasion else None
        self.attacker = AttackerDefender(json_invasion['attacker']) if 'attacker' in json_invasion else None
        self.attacker_reward = Reward(json_invasion['attackerReward']) if 'attackerReward' in json_invasion else None
        self.attacking_faction = str(json_invasion['attackingFaction']) if 'attackingFaction' in json_invasion else None
        self.completed = bool(json_invasion['completed']) if 'completed' in json_invasion else None
        self.completion = list[int](json_invasion['completion']) if 'completion' in json_invasion else []
        self.count = int(json_invasion['count']) if 'count' in json_invasion else None
        self.defender = AttackerDefender(json_invasion['defender']) if 'defender' in json_invasion else None
        self.defender_reward = Reward(json_invasion['defenderReward']) if 'defenderReward' in json_invasion else None
        self.defending_faction = str(json_invasion['defendingFaction']) if 'defendingFaction' in json_invasion else None
        self.desc = str(json_invasion['desc']) if 'desc' in json_invasion else None
        self.eta = str(json_invasion['eta']) if 'eta' in json_invasion else None
        self.node = str(json_invasion['node']) if 'node' in json_invasion else None
        self.node_key = str(json_invasion['nodeKey']) if 'nodeKey' in json_invasion else None
        self.required_runs = int(json_invasion['requiredRuns']) if 'requiredRuns' in json_invasion else None
        self.reward_types = list[str](json_invasion['rewardTypes']) if 'rewardTypes' in json_invasion else []
        self.vs_infestation = bool(json_invasion['vsInfestation']) if 'vsInfestation' in json_invasion else None