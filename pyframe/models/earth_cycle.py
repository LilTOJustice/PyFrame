from pyframe.models.common import WarframeObj, isoparse

class EarthCycle(WarframeObj):
    def __init__(self, json_earth_cycle: dict):
        self.id = str(json_earth_cycle['id']) if 'id' in json_earth_cycle else None
        self.activation = isoparse(json_earth_cycle['activation']) if 'activation' in json_earth_cycle else None
        self.expiration = isoparse(json_earth_cycle['expiry']) if 'expiry' in json_earth_cycle else None
        self.start_string = str(json_earth_cycle['startString']) if 'startString' in json_earth_cycle else None
        self.active = bool(json_earth_cycle['active']) if 'active' in json_earth_cycle else None
        self.is_day = bool(json_earth_cycle['isDay']) if 'isDay' in json_earth_cycle else None
        self.time_left = str(json_earth_cycle['timeLeft']) if 'timeLeft' in json_earth_cycle else None