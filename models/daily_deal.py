from models.common import WarframeObj
from collections import defaultdict
from dateutil.parser import isoparse

class DailyDeal(WarframeObj):
    def __init__(self, json_daily_deal: dict):
        json_daily_deal = defaultdict(lambda : None, json_daily_deal)
        self.sold = json_daily_deal['sold']
        self.item = json_daily_deal['item']
        self.unique_name = json_daily_deal['uniqueName']
        self.total = json_daily_deal['total']
        self.eta = json_daily_deal['eta']
        self.original_price = json_daily_deal['originalPrice']
        self.sale_price = json_daily_deal['salePrice']
        self.discount  = json_daily_deal['discount']
        self.expiry = isoparse(json_daily_deal['expiry']) if 'expiry' in json_daily_deal else None
        self.id = json_daily_deal['id']
        