from pyframe.models.common import WarframeObj
from collections import defaultdict

class GlobalUpgrade(WarframeObj):
    def __init__(self, json_global_upgrade: dict):
        json_global_upgrade = defaultdict(lambda : None, json_global_upgrade)
        self.start = json_global_upgrade['start']
        self.end = json_global_upgrade['end']
        self.upgrade = json_global_upgrade['upgrade']
        self.operation = json_global_upgrade['operation']
        self.operation_symbol = json_global_upgrade['operationSymbol']
        self.upgrade_operation_value = json_global_upgrade['upgradeOperationSymbol']
        self.expired = json_global_upgrade['expired']
        self.eta = json_global_upgrade['eta']
        self.desc = json_global_upgrade['desc']
