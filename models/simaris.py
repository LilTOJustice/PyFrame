from collections import defaultdict
from models.common import WarframeObj

class Simaris(WarframeObj):
    def __init__(self, json_simaris: dict):
        json_simaris = defaultdict(lambda : None, json_simaris)
        self.target = json_simaris['target']
        self.is_target_active = json_simaris['isTargetActive']
        self.as_string = json_simaris['asString']