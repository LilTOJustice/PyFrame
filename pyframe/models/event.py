from pyframe.models.common import Reward, WarframeObj, Job
from dateutil.parser import isoparse

class Message(WarframeObj):
    def __init__(self, json_message: dict):
        self.sender = str(json_message['sender']) if 'sender' in json_message else None
        self.subject = str(json_message['subject']) if 'subject' in json_message else None
        self.message = str(json_message['message']) if 'message' in json_message else None
        self.sender_icon = str(json_message['senderIcon']) if 'senderIcon' in json_message else None
        self.attachments = list[str](json_message['attachments']) if 'attachments' in json_message else []

class InterimStep(WarframeObj):
    def __init__(self, json_interim_step: dict):
        self.goal = int(json_interim_step['goal']) if 'goal' in json_interim_step else None
        self.reward = Reward(json_interim_step['reward']) if 'reward' in json_interim_step else None
        self.message = Message(json_interim_step['message']) if 'message' in json_interim_step else None
        self.winner_count = int(json_interim_step['winnerCount']) if 'winnerCount' in json_interim_step else None

class ProgressStep(WarframeObj):
    def __init__(self, json_progress_step: dict):
        self.type = str(json_progress_step['type']) if 'type' in json_progress_step else None
        self.progress_amt = int(json_progress_step['progressAmt']) if 'progressAmt' in json_progress_step else None

class Alt(WarframeObj):
    def __init__(self, json_alt: dict):
        self.expiry = isoparse(json_alt['expiry']) if 'expiry' in json_alt else None
        self.activation = isoparse(json_alt['activation']) if 'activation' in json_alt else None

class Event(WarframeObj):
    def __init__(self, json_event: dict):
        self.id = str(json_event['id']) if 'id' in json_event else None
        self.activation = isoparse(json_event['activation']) if 'activation' in json_event else None
        self.expiry = isoparse(json_event['expiry']) if 'expiry' in json_event else None
        self.start_string = str(json_event['startString']) if 'startString' in json_event else None
        self.active = bool(json_event['active']) if 'active' in json_event else None
        self.maximum_score = int(json_event['maximumScore']) if 'maximumScore' in json_event else None
        self.current_score = int(json_event['currentScore']) if 'currentScore' in json_event else None
        self.small_interval = int(json_event['smallInterval']) if 'smallInterval' in json_event else None
        self.large_interval = int(json_event['largeInterval']) if 'largeInterval' in json_event else None
        self.faction = str(json_event['faction']) if 'faction' in json_event else None
        self.description = str(json_event['description']) if 'description' in json_event else None
        self.tooltip = str(json_event['tooltip']) if 'tooltip' in json_event else None
        self.node = str(json_event['node']) if 'node' in json_event else None
        self.concurrent_nodes = list[str](json_event['concurrent_nodes']) if 'concurrent_nodes' in json_event else []
        self.victim_node = str(json_event['victimNode']) if 'victimNode' in json_event else None
        self.score_loc_tag = str(json_event['scoreLocTag']) if 'scoreLocTag' in json_event else None
        self.rewards = [Reward(reward) for reward in json_event['rewards']] if 'rewards' in json_event else []
        self.health = int(json_event['health']) if 'health' in json_event else None
        self.affiliated_with = str(json_event['affiliatedWith']) if 'affiliatedWith' in json_event else None
        self.jobs = [Job(job) for job in json_event['jobs']] if 'jobs' in json_event else []
        self.interim_steps = [InterimStep(interim_step) for interim_step in json_event['interimSteps']] if 'interimSteps' in json_event else []
        self.progress_steps = [ProgressStep(progress_step) for progress_step in json_event['progressSteps']] if 'progressSteps' in json_event else []
        self.progress_total = int(json_event['progressTotal']) if 'progressTotal' in json_event else None
        self.show_total_at_end_of_mission = bool(json_event['showTotalAtEndOfMission']) if 'showTotalAtEndOfMission' in json_event else None
        self.is_personal = bool(json_event['isPersonal']) if 'isPersonal' in json_event else None
        self.is_comminity = bool(json_event['isCommunity']) if 'isCommunity' in json_event else None
        self.region_drops = list[str](json_event['regionDrops']) if 'regionDrops' in json_event else []
        self.archwing_drops = list[str](json_event['archwingDrops']) if 'archwingDrops' in json_event else []
        self.as_string = str(json_event['asString']) if 'asString' in json_event else None
        self.metadata = dict[str, any](json_event['metadata']) if 'metadata' in json_event else {}
        self.completion_bonuses = list[int](json_event['completionBonuses']) if 'completionBonuses' in json_event else []
        self.score_var = str(json_event['scoreVar']) if 'scoreVar' in json_event else None
        self.alt_expiry = str(json_event['altExpiry']) if 'altExpiry' in json_event else None
        self.alt_activation = str(json_event['altActivation']) if 'altActivation' in json_event else None
        self.next_alt = Alt(json_event['nextAlt']) if 'nextAlt' in json_event else None