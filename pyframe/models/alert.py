from pyframe.models.common import Mission, WarframeObj, isoparse

class Alert(WarframeObj):
    def __init__(self, json_alert: dict):
        self.id = str(json_alert['id']) if 'id' in json_alert else None
        self.activation = isoparse(json_alert['activation']) if 'activation' in json_alert else None
        self.expiry = isoparse(json_alert['expiry']) if 'expiry' in json_alert else None
        self.start_string = str(json_alert['startString']) if 'startString' in json_alert else None
        self.active = bool(json_alert['active']) if 'active' in json_alert else None
        self.mission = Mission(json_alert['mission']) if 'mission' in json_alert else None
        self.expired = bool(json_alert['expired']) if 'expired' in json_alert else None
        self.eta = str(json_alert['eta']) if 'eta' in json_alert else None
        self.reward_types = list[str](json_alert['rewardTypes']) if 'rewardTypes' in json_alert else []