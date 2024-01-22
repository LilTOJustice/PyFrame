from collections import defaultdict
from dateutil.parser import isoparse
from models.common import WarframeObj

class VoidTrader(WarframeObj):
    def __init__(self, json_void_trader: dict):
        json_void_trader = defaultdict(lambda : None, json_void_trader)
        self.id = json_void_trader['id']
        self.activation = isoparse(json_void_trader['activation']) if 'activation' in json_void_trader else None
        self.expiry = isoparse(json_void_trader['expiry']) if 'expiry' in json_void_trader else None
        self.start_string = json_void_trader['startString']
        self.active = json_void_trader['active']
        self.character = json_void_trader['character']
        self.location = json_void_trader['location']
        self.inventory = [VoidTraderItem(item) for item in json_void_trader['inventory']] if 'inventory' in json_void_trader else []
        self.ps_id = json_void_trader['psId']
        self.end_string = json_void_trader['endString']

class VoidTraderItem(WarframeObj):
    def __init__(self, json_void_trader_item):
        json_void_trader_item = defaultdict(lambda : None, json_void_trader_item)
        self.item = json_void_trader_item['item']
        self.ducats = json_void_trader_item['ducats']
        self.credits = json_void_trader_item['credits']