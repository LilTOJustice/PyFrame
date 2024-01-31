from pyframe.models.common import WarframeObj

class PersistentEnemy(WarframeObj):
    def __init__(self, json_persistent_enemy: dict):
        self.location_tag = str(json_persistent_enemy['locationTag']) if 'locationTag' in json_persistent_enemy else None
        self.agent_type = str(json_persistent_enemy['agentType']) if 'agentType' in json_persistent_enemy else None
        self.rank = int(json_persistent_enemy['rank']) if 'rank' in json_persistent_enemy else None
        self.health_percent = int(json_persistent_enemy['healthPercent']) if 'healthPercent' in json_persistent_enemy else None
        self.flee_damage = int(json_persistent_enemy['fleeDamage']) if 'fleeDamage' in json_persistent_enemy else None
        self.region = str(json_persistent_enemy['region']) if 'region' in json_persistent_enemy else None
        self.last_discovered_time = str(json_persistent_enemy['lastDiscoveredTime']) if 'lastDiscoveredTime' in json_persistent_enemy else None
        self.last_discovered_at = str(json_persistent_enemy['lastDiscoveredAt']) if 'lastDiscoveredAt' in json_persistent_enemy else None
        self.is_discovered = bool(json_persistent_enemy['isDiscovered']) if 'isDiscovered' in json_persistent_enemy else None
        self.is_using_ticketing = bool(json_persistent_enemy['isUsingTicketing']) if 'isUsingTicketing' in json_persistent_enemy else None
        self.pid = str(json_persistent_enemy['pid']) if 'pid' in json_persistent_enemy else None
