from pyframe.models.common import WarframeObj

class Simaris(WarframeObj):
    def __init__(self, json_simaris: dict):
        self.target = str(json_simaris['target']) if 'target' in json_simaris else None
        self.is_target_active = bool(json_simaris['isTargetActive']) if 'isTargetActive' in json_simaris else None
        self.as_string = str(json_simaris['asString']) if 'asString' in json_simaris else None