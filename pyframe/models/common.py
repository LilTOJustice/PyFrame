from collections import defaultdict
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
        json_counted_item = defaultdict(lambda : None, json_counted_item)
        self.count = json_counted_item['count']
        self.type = json_counted_item['type']

class Job(WarframeObj):
    def __init__(self, json_job: dict):
        json_job = defaultdict(lambda : None, json_job)
        self.activation = isoparse(json_job['activation']) if 'activation' in json_job else None
        self.expiry = isoparse(json_job['expiry']) if 'expiry' in json_job else None
        self.reward_pool = json_job['reward_pool'] if 'reward_pool' in json_job else []
        self.type = json_job['type']
        self.enemy_levels = json_job['enemyLevels'] if 'enemyLevels' in json_job else []
        self.standing_stages = json_job['standingStages'] if 'standingStages' in json_job else []
        self.minMR = json_job['minMR']

class Reward(WarframeObj):
    def __init__(self, json_reward: dict):
        json_reward = defaultdict(lambda : None, json_reward)
        self.counted_items = [CountedItem(counted_item) for counted_item in json_reward['countedItems']] if 'countedItems' in json_reward else []
        self.thumbnail = json_reward['thumbnail']
        self.color = json_reward['color']
        self.credits = json_reward['credits']
        self.as_string = json_reward['asString']
        self.items = json_reward['items']
        self.item_string = json_reward['itemString']

class Mission(WarframeObj):
    def __init__(self, json_mission: dict):
        json_mission = defaultdict(lambda : None, json_mission)
        self.reward = Reward(json_mission['reward']) if 'reward' in json_mission else None
        self.node = json_mission['node']
        self.node_key = json_mission['nodeKey']
        self.faction = json_mission['faction']
        self.faction_key = json_mission['factionKey']
        self.max_enemy_level = json_mission['maxEnemyLevel']
        self.min_enemy_level = json_mission['minEnemyLevel']
        self.max_wave_num = json_mission['maxWaveNum']
        self.type = json_mission['type']
        self.type_key = json_mission['typeKey']
        self.nightmare = json_mission['nightmare']
        self.archwing_required = json_mission['archwingRequired']
        self.is_sharkwing = json_mission['isSharkwing']
        self.enemy_spec = json_mission['enemySpec']
        self.level_override = json_mission['levelOverride']
        self.advanced_spawners = json_mission['advancedSpawners']
        self.required_items = json_mission['requiredItems']
        self.consume_required_items = json_mission['consumeRequiredItems']
        self.leaders_always_allowed = json_mission['leadersAlwaysAllowed']
        self.level_auras = json_mission['levelAuras']
        self.description = json_mission['description']