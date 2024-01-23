from collections import defaultdict
from dateutil.parser import isoparse
from models.common import WarframeObj, Job

class SyndicateMission(WarframeObj):
    def __init__(self, json_syndicate_mission: dict):
        json_syndicate_mission = defaultdict(lambda : None, json_syndicate_mission)
        self.nodes = json_syndicate_mission['nodes'] if 'nodes' in json_syndicate_mission else []
        self.eta = json_syndicate_mission['eta']
        self.jobs = [Job(job) for job in json_syndicate_mission['jobs']] if 'jobs' in json_syndicate_mission else []
        self.syndicate = json_syndicate_mission['syndicate']
        self.id = json_syndicate_mission['id']
        self.expiry = isoparse(json_syndicate_mission['expiry']) if 'expiry' in json_syndicate_mission else None
        self.activation = isoparse(json_syndicate_mission['activation']) if 'activation' in json_syndicate_mission else None
