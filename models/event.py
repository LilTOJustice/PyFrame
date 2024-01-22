from collections import defaultdict
from models.common import Reward, WarframeObj, Job
from dateutil.parser import isoparse

class Message(WarframeObj):
    def __init__(self, json_message: dict):
        json_message = defaultdict(lambda : None, json_message)
        self.sender = json_message['sender']
        self.subject = json_message['subject']
        self.message = json_message['message']
        self.sender_icon = json_message['senderIcon']
        self.attachments = json_message['attachments'] if 'attachments' in json_message else []

class InterimStep(WarframeObj):
    def __init__(self, json_interim_step: dict):
        json_interim_step = defaultdict(lambda : None, json_interim_step)
        self.goal = json_interim_step['goal']
        self.reward = Reward(json_interim_step['reward']) if 'reward' in json_interim_step else None
        self.message = Message(json_interim_step['message']) if 'message' in json_interim_step else None
        self.winner_count = json_interim_step['winnerCount']

class ProgressStep(WarframeObj):
    def __init__(self, json_progress_step: dict):
        json_progress_step = defaultdict(lambda : None, json_progress_step)
        self.type = json_progress_step['type']
        self.progress_amt = json_progress_step['progressAmt']

class Alt(WarframeObj):
    def __init__(self, json_alt: dict):
        json_alt = defaultdict(lambda : None, json_alt)
        self.expiry = isoparse(json_alt['expiry']) if 'expiry' in json_alt else None
        self.activation = isoparse(json_alt['activation']) if 'activation' in json_alt else None

class Event(WarframeObj):
    def __init__(self, json_event: dict):
        json_event = defaultdict(lambda : None, json_event)
        self.id = json_event['id']
        self.activation = isoparse(json_event['activation']) if 'activation' in json_event else None
        self.expiry = isoparse(json_event['expiry']) if 'expiry' in json_event else None
        self.start_string = json_event['startString']
        self.active = json_event['active']
        self.maximum_score = json_event['maximumScore']
        self.current_score = json_event['currentScore']
        self.small_interval = json_event['smallInterval']
        self.large_interval = json_event['largeInterval']
        self.faction = json_event['faction']
        self.description = json_event['description']
        self.tooltip = json_event['tooltip']
        self.node = json_event['node']
        self.concurrent_nodes = json_event['concurrent_nodes'] if 'concurrent_nodes' in json_event else []
        self.victim_node = json_event['victimNode']
        self.score_loc_tag = json_event['scoreLocTag']
        self.rewards = [Reward(reward) for reward in json_event['rewards']] if 'rewards' in json_event else []
        self.health = json_event['health']
        self.affiliated_with = json_event['affiliatedWith']
        self.jobs = [Job(job) for job in json_event['jobs']] if 'jobs' in json_event else []
        self.interim_steps = [InterimStep(interim_step) for interim_step in json_event['interimSteps']] if 'interimSteps' in json_event else []
        self.progress_steps = [ProgressStep(progress_step) for progress_step in json_event['progressSteps']] if 'progressSteps' in json_event else []
        self.progress_total = json_event['progressTotal']
        self.show_total_at_end_of_mission = json_event['showTotalAtEndOfMission']
        self.is_personal = json_event['isPersonal']
        self.is_comminity = json_event['isCommunity']
        self.region_drops = json_event['regionDrops'] if 'regionDrops' in json_event else []
        self.archwing_drops = json_event['archwingDrops'] if 'archwingDrops' in json_event else []
        self.as_string = json_event['asString']
        self.metadata = json_event['metadata']
        self.completion_bonuses = json_event['completionBonuses'] if 'completionBonuses' in json_event else []
        self.score_var = json_event['scoreVar']
        self.alt_expiry = json_event['altExpiry']
        self.alt_activation = json_event['altActivation']
        self.next_alt = Alt(json_event['nextAlt']) if 'nextAlt' in json_event else None