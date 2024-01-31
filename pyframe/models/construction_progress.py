from pyframe.models.common import WarframeObj

class ConstructionProgress(WarframeObj):
    def __init__(self, json_construction_progress: dict):
        self.id = str(json_construction_progress['id']) if 'id' in json_construction_progress else None
        self.fomorian_progress = str(json_construction_progress['fomorianProgress']) if 'fomorianProgress' in json_construction_progress else None
        self.razorback_progress = str(json_construction_progress['razorbackProgress']) if 'razorbackProgress' in json_construction_progress else None
        self.unknown_progress = str(json_construction_progress['unkownProgress']) if 'unkownProgress' in json_construction_progress else None
    