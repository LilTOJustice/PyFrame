from pyframe.models.common import WarframeObj, isoparse

class Challenge(WarframeObj):
    def __init__(self, json_challenge: dict):
        self.id = str(json_challenge['id']) if 'id' in json_challenge else None
        self.activation = isoparse(json_challenge['activation']) if 'activation' in json_challenge else None
        self.expiry = isoparse(json_challenge['expiry']) if 'expiry' in json_challenge else None
        self.start_string = str(json_challenge['startString']) if 'startString' in json_challenge else None
        self.active = bool(json_challenge['active']) if 'active' in json_challenge else None
        self.is_daily = bool(json_challenge['isDaily']) if 'isDaily' in json_challenge else None
        self.is_elite = bool(json_challenge['isElite']) if 'isElite' in json_challenge else None
        self.title = str(json_challenge['title']) if 'title' in json_challenge else None
        self.desc = str(json_challenge['desc']) if 'desc' in json_challenge else None
        self.reputation = int(json_challenge['reputation']) if 'reputation' in json_challenge else None

class Nightwave(WarframeObj):
    def __init__(self, json_nightwave: dict):
        self.id = str(json_nightwave['id']) if 'id' in json_nightwave else None
        self.activation = isoparse(json_nightwave['activation']) if 'activation' in json_nightwave else None
        self.expiry = isoparse(json_nightwave['expiry']) if 'expiry' in json_nightwave else None
        self.start_string = str(json_nightwave['startString']) if 'startString' in json_nightwave else None
        self.active = bool(json_nightwave['active']) if 'active' in json_nightwave else None
        self.params = dict[str, any](json_nightwave['params']) if 'params' in json_nightwave else {}
        self.reward_types = list[str](json_nightwave['rewardTypes']) if 'rewardTypes' in json_nightwave else []
        self.season = int(json_nightwave['season']) if 'season' in json_nightwave else None
        self.tag = str(json_nightwave['tag']) if 'tag' in json_nightwave else None
        self.phase = int(json_nightwave['phase']) if 'phase' in json_nightwave else None
        self.possible_challenges = [Challenge(challenge) for challenge in json_nightwave['possibleChallenges']] if 'possibleChallenges' in json_nightwave else []
        self.active_challenges = [Challenge(challenge) for challenge in json_nightwave['activeChallenges']] if 'activeChallenges' in json_nightwave else []