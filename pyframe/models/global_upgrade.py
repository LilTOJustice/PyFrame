from pyframe.models.common import WarframeObj
from dateutil.parser import isoparse

class GlobalUpgrade(WarframeObj):
    def __init__(self, json_global_upgrade: dict):
        self.start = isoparse(json_global_upgrade['start']) if 'start' in json_global_upgrade else None
        self.end = isoparse(json_global_upgrade['end']) if 'end' in json_global_upgrade else None
        self.upgrade = str(json_global_upgrade['upgrade']) if 'upgrade' in json_global_upgrade else None
        self.operation = str(json_global_upgrade['operation']) if 'operation' in json_global_upgrade else None
        self.operation_symbol = str(json_global_upgrade['operationSymbol']) if 'operationSymbol' in json_global_upgrade else None
        self.upgrade_operation_value = int(json_global_upgrade['upgradeOperationSymbol']) if 'upgradeOperationSymbol' in json_global_upgrade else None
        self.expired = bool(json_global_upgrade['expired']) if 'expired' in json_global_upgrade else None
        self.eta = str(json_global_upgrade['eta']) if 'eta' in json_global_upgrade else None
        self.desc = str(json_global_upgrade['desc']) if 'desc' in json_global_upgrade else None
