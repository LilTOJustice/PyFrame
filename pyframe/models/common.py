from pprint import PrettyPrinter
from dateutil.parser import isoparse

pp = PrettyPrinter(indent = 4, width = 150)

class WarframeObj:
    def __str__(self):
        return pp.pformat(self.__dict__)
    
    def __repr__(self):
        return self.__str__()

class CountedItem(WarframeObj):
    def __init__(self, json_counted_item: dict):
        self.count = int(json_counted_item['count']) if 'count' in json_counted_item else None
        self.type = str(json_counted_item['type']) if 'type' in json_counted_item else None

class Job(WarframeObj):
    def __init__(self, json_job: dict):
        self.activation = isoparse(json_job['activation']) if 'activation' in json_job else None
        self.expiry = isoparse(json_job['expiry']) if 'expiry' in json_job else None
        self.reward_pool = list[str](json_job['reward_pool']) if 'reward_pool' in json_job else []
        self.type = str(json_job['type']) if 'type' in json_job else None
        self.enemy_levels = list[int](json_job['enemyLevels']) if 'enemyLevels' in json_job else []
        self.standing_stages = list[int](json_job['standingStages']) if 'standingStages' in json_job else []
        self.min_mastery_rank = int(json_job['minMR']) if 'minMR' in json_job else None

class Reward(WarframeObj):
    def __init__(self, json_reward: dict):
        self.counted_items = [CountedItem(counted_item) for counted_item in json_reward['countedItems']] if 'countedItems' in json_reward else []
        self.thumbnail = str(json_reward['thumbnail']) if 'thumbnail' in json_reward else None
        self.color = int(json_reward['color']) if 'color' in json_reward else None
        self.credits = int(json_reward['credits']) if 'credits' in json_reward else None
        self.as_string = str(json_reward['asString']) if 'asString' in json_reward else None
        self.items = list[str](json_reward['items']) if 'items' in json_reward else []
        self.item_string = str(json_reward['itemString']) if 'itemString' in json_reward else None

class Mission(WarframeObj):
    def __init__(self, json_mission: dict):
        self.reward = Reward(json_mission['reward']) if 'reward' in json_mission else None
        self.node = str(json_mission['node']) if 'node' in json_mission else None
        self.node_key = str(json_mission['nodeKey']) if 'nodeKey' in json_mission else None
        self.faction = str(json_mission['faction']) if 'faction' in json_mission else None
        self.faction_key = str(json_mission['factionKey']) if 'factionKey' in json_mission else None
        self.max_enemy_level = int(json_mission['maxEnemyLevel']) if 'maxEnemyLevel' in json_mission else None
        self.min_enemy_level = int(json_mission['minEnemyLevel']) if 'minEnemyLevel' in json_mission else None
        self.max_wave_num = int(json_mission['maxWaveNum']) if 'maxWaveNum' in json_mission else None
        self.type = str(json_mission['type']) if 'type' in json_mission else None
        self.type_key = str(json_mission['typeKey']) if 'typeKey' in json_mission else None
        self.nightmare = bool(json_mission['nightmare']) if 'nightmare' in json_mission else None
        self.archwing_required = bool(json_mission['archwingRequired']) if 'archwingRequired' in json_mission else None
        self.is_sharkwing = bool(json_mission['isSharkwing']) if 'isSharkwing' in json_mission else None
        self.enemy_spec = str(json_mission['enemySpec']) if 'enemySpec' in json_mission else None
        self.level_override = str(json_mission['levelOverride']) if 'levelOverride' in json_mission else None
        self.advanced_spawners = list[str](json_mission['advancedSpawners'])
        self.required_items = list[str](json_mission['requiredItems'])
        self.consume_required_items = bool(json_mission['consumeRequiredItems']) if 'consumeRequiredItems' in json_mission else None
        self.leaders_always_allowed = bool(json_mission['leadersAlwaysAllowed']) if 'leadersAlwaysAllowed' in json_mission else None
        self.level_auras = list[str](json_mission['levelAuras']) if 'levelAuras' in json_mission else []
        self.description = str(json_mission['description']) if 'description' in json_mission else None