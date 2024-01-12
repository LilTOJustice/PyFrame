from collections import defaultdict
from dateutil.parser import isoparse
from models.common import Mission

class Alert:
    def __init__(self, json_alert: dict):
        json_alert = defaultdict(lambda : None, json_alert)
        self.id = json_alert['id']
        self.activation = isoparse(json_alert['activation']) if 'activation' in json_alert else None
        self.expiry = isoparse(json_alert['expiry']) if 'expiry' in json_alert else None
        self.start_string = json_alert['startString']
        self.active = json_alert['active']
        self.mission = Mission(json_alert['mission']) if 'mission' in json_alert else None
        self.expired = json_alert['expired']
        self.eta = json_alert['eta']
        self.reward_types = json_alert['rewardTypes']

    def __str__(self):
        return self.__dict__