from collections import defaultdict
from dateutil.parser import isoparse
from models.common import WarframeObj

class PersistentEnemy(WarframeObj):
    def __init__(self, json_persistent_enemy : dict):
        json_persistent_enemy = defaultdict(lambda : None, json_persistent_enemy)
        self.location_tag = json_persistent_enemy['locationTag']
        self.agent_type = json_persistent_enemy['agentType']
        self.rank = json_persistent_enemy['rank']
        self.health_percent = json_persistent_enemy['healthPercent']
        self.flee_damage = json_persistent_enemy['flee_damage']
        self.region = json_persistent_enemy['region']
        self.last_discovered_time = json_persistent_enemy['lastDiscoveredTime']
        self.last_discovered_at = json_persistent_enemy['lastDiscoveredAt']
        self.is_discovered = json_persistent_enemy['isDiscovered']
        self.is_using_ticketing = json_persistent_enemy['isUsingTicketing']
        self.pid = json_persistent_enemy['pid']