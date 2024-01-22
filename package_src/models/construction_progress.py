from models.common import WarframeObj
from collections import defaultdict

class ConstructionProgress(WarframeObj):
    def __init__(self, json_construction_progress: dict):
        json_construction_progress = defaultdict(lambda : None, json_construction_progress)
        self.id = json_construction_progress['id']
        self.fomorian_progress = json_construction_progress['fomorianProgress']
        self.razorback_progress = json_construction_progress['razorbackProgress']
        self.unknown_progress = json_construction_progress['unkownProgress']
    