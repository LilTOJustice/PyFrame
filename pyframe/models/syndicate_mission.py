from pyframe.models.common import WarframeObj, Job, isoparse

class SyndicateMission(WarframeObj):
    def __init__(self, json_syndicate_mission: dict):
        self.nodes = list[str](json_syndicate_mission['nodes']) if 'nodes' in json_syndicate_mission else []
        self.eta = str(json_syndicate_mission['eta']) if 'eta' in json_syndicate_mission else None
        self.jobs = [Job(job) for job in json_syndicate_mission['jobs']] if 'jobs' in json_syndicate_mission else []
        self.syndicate = str(json_syndicate_mission['syndicate']) if 'syndicate' in json_syndicate_mission else None
        self.id = str(json_syndicate_mission['id']) if 'id' in json_syndicate_mission else None
        self.expiry = isoparse(json_syndicate_mission['expiry']) if 'expiry' in json_syndicate_mission else None
        self.activation = isoparse(json_syndicate_mission['activation']) if 'activation' in json_syndicate_mission else None
