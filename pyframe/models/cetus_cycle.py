from pyframe.models.common import WarframeObj, isoparse

class CetusCycle(WarframeObj):
    def __init__(self, json_cetus_cycle: dict):
        self.id = str(json_cetus_cycle['id']) if 'id' in json_cetus_cycle else None
        self.activation = isoparse(json_cetus_cycle['activation']) if 'activation' in json_cetus_cycle else None
        self.expiry = isoparse(json_cetus_cycle['expiry']) if 'expiry' in json_cetus_cycle else None
        self.start_string = str(json_cetus_cycle['startString']) if 'startString' in json_cetus_cycle else None
        self.active = bool(json_cetus_cycle['active']) if 'active' in json_cetus_cycle else None
        self.is_day = bool(json_cetus_cycle['isDay']) if 'isDay' in json_cetus_cycle else None
        self.state = str(json_cetus_cycle['state']) if 'state' in json_cetus_cycle else None
        self.time_left = str(json_cetus_cycle['timeLeft']) if 'timeLeft' in json_cetus_cycle else None
        self.is_cetus = bool(json_cetus_cycle['isCetus']) if 'isCetus' in json_cetus_cycle else None
        self.short_string = str(json_cetus_cycle['shortString']) if 'shortString' in json_cetus_cycle else None
