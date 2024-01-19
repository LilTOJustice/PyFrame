from collections import defaultdict
from dateutil.parser import isoparse
from models.common import WarframeObj, Job

class SyndicateMission(WarframeObj):
    def __init__(self, json_syndicate: dict):
        json_syndicate = defaultdict(lambda : None, json_syndicate)
        self.nodes = json_syndicate['nodes'] if 'nodes' in json_syndicate else []
        self.eta = json_syndicate['eta']
        self.jobs = [Job(job) for job in json_syndicate['jobs']] if 'jobs' in json_syndicate else []
        self.syndicate = json_syndicate['syndicate']
        self.id = json_syndicate['id']
        self.expiry = json_syndicate['expiry']
        self.activation = isoparse(json_syndicate['activation']) if 'activation' in json_syndicate else None
