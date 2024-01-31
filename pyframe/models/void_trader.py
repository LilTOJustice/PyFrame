from dateutil.parser import isoparse
from pyframe.models.common import WarframeObj

class VoidTrader(WarframeObj):
    def __init__(self, json_void_trader: dict):
        self.id = str(json_void_trader['id']) if 'id' in json_void_trader else None
        self.activation = isoparse(json_void_trader['activation']) if 'activation' in json_void_trader else None
        self.expiry = isoparse(json_void_trader['expiry']) if 'expiry' in json_void_trader else None
        self.start_string = str(json_void_trader['startString']) if 'startString' in json_void_trader else None
        self.active = bool(json_void_trader['active']) if 'active' in json_void_trader else None
        self.character = str(json_void_trader['character']) if 'character' in json_void_trader else None
        self.location = str(json_void_trader['location']) if 'location' in json_void_trader else None
        self.inventory = [VoidTraderItem(item) for item in json_void_trader['inventory']] if 'inventory' in json_void_trader else []
        self.ps_id = str(json_void_trader['psId']) if 'psId' in json_void_trader else None
        self.end_string = str(json_void_trader['endString']) if 'endString' in json_void_trader else None

class VoidTraderItem(WarframeObj):
    def __init__(self, json_void_trader_item):
        self.item = str(json_void_trader_item['item']) if 'item' in json_void_trader_item else None
        self.ducats = int(json_void_trader_item['ducats']) if 'ducats' in json_void_trader_item else None
        self.credits = int(json_void_trader_item['credits']) if 'credits' in json_void_trader_item else None