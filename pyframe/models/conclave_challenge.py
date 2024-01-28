from collections import defaultdict
from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class ConclaveChallenge(WarframeObj):
    def __init__(self, json_conclave_challenge: dict):
        json_conclave_challenge = defaultdict(lambda : None, json_conclave_challenge)
        self.mode = json_conclave_challenge['mode']
        self.amount = json_conclave_challenge['amount']
        self.eta = json_conclave_challenge['eta']
        self.expired = json_conclave_challenge['expired']
        self.end_string = json_conclave_challenge['endString']
        self.daily = json_conclave_challenge['daily']
        self.description = json_conclave_challenge['description']
        self.id = json_conclave_challenge['id']
        self.expiry = isoparse(json_conclave_challenge['expiry']) if 'expiry' in json_conclave_challenge else None
        self.as_string = json_conclave_challenge['asString']
        self.category = json_conclave_challenge['category']
        self.root_challenge = json_conclave_challenge['rootChallenge']