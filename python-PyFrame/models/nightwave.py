from collections import defaultdict
from models.common import WarframeObj
from dateutil.parser import isoparse

class Challenge(WarframeObj):
    def __init__(self, json_challenge: dict):
        json_challenge = defaultdict(lambda : None, json_challenge)
        self.id = json_challenge['id']
        self.activation = isoparse(json_challenge['activation']) if 'activation' in json_challenge else None
        self.expiry = isoparse(json_challenge['expiry']) if 'expiry' in json_challenge else None
        self.start_string = json_challenge['startString']
        self.active = json_challenge['active']
        self.is_daily = json_challenge['isDaily']
        self.is_elite = json_challenge['isElite']
        self.title = json_challenge['title']
        self.desc = json_challenge['desc']
        self.reputation = json_challenge['reputation']

class Nightwave(WarframeObj):
    def __init__(self, json_nightwave: dict):
        json_nightwave = defaultdict(lambda : None, json_nightwave)
        self.id = json_nightwave['id']
        self.activation = isoparse(json_nightwave['activation']) if 'activation' in json_nightwave else None
        self.expiry = isoparse(json_nightwave['expiry']) if 'expiry' in json_nightwave else None
        self.start_string = json_nightwave['startString']
        self.active = json_nightwave['active']
        self.params = json_nightwave['params']
        self.reward_types = json_nightwave['rewardTypes'] if 'rewardTypes' in json_nightwave else []
        self.season = json_nightwave['season']
        self.tag = json_nightwave['tag']
        self.possible_challenges = [Challenge(challenge) for challenge in json_nightwave['possibleChallenges']] if 'possibleChallenges' in json_nightwave else []
        self.active_challenges = [Challenge(challenge) for challenge in json_nightwave['activeChallenges']] if 'activeChallenges' in json_nightwave else []