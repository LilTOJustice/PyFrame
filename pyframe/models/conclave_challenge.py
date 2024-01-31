from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class ConclaveChallenge(WarframeObj):
    def __init__(self, json_conclave_challenge: dict):
        self.mode = str(json_conclave_challenge['mode']) if 'mode' in json_conclave_challenge else None
        self.amount = int(json_conclave_challenge['amount']) if 'amount' in json_conclave_challenge else None
        self.eta = str(json_conclave_challenge['eta']) if 'eta' in json_conclave_challenge else None
        self.expired = bool(json_conclave_challenge['expired']) if 'expired' in json_conclave_challenge else None
        self.end_string = str(json_conclave_challenge['endString']) if 'endString' in json_conclave_challenge else None
        self.daily = bool(json_conclave_challenge['daily']) if 'daily' in json_conclave_challenge else None
        self.description = str(json_conclave_challenge['description']) if 'description' in json_conclave_challenge else None
        self.id = str(json_conclave_challenge['id']) if 'id' in json_conclave_challenge else None
        self.expiry = isoparse(json_conclave_challenge['expiry']) if 'expiry' in json_conclave_challenge else None
        self.as_string = str(json_conclave_challenge['asString']) if 'asString' in json_conclave_challenge else None
        self.category = str(json_conclave_challenge['category']) if 'category' in json_conclave_challenge else None
        self.root_challenge = bool(json_conclave_challenge['rootChallenge']) if 'rootChallenge' in json_conclave_challenge else None