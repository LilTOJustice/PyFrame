from pyframe.models.common import WarframeObj, isoparse

class DailyDeal(WarframeObj):
    def __init__(self, json_daily_deal: dict):
        self.sold = int(json_daily_deal['sold'])
        self.item = str(json_daily_deal['item']) if 'item' in json_daily_deal else None
        self.unique_name = str(json_daily_deal['uniqueName']) if 'uniqueName' in json_daily_deal else None
        self.total = int(json_daily_deal['total']) if 'total' in json_daily_deal else None
        self.eta = str(json_daily_deal['eta']) if 'eta' in json_daily_deal else None
        self.original_price = int(json_daily_deal['originalPrice']) if 'originalPrice' in json_daily_deal else None
        self.sale_price = int(json_daily_deal['salePrice']) if 'salePrice' in json_daily_deal else None
        self.discount  = int(json_daily_deal['discount']) if 'discount' in json_daily_deal else None
        self.expiry = isoparse(json_daily_deal['expiry']) if 'expiry' in json_daily_deal else None
        self.id = str(json_daily_deal['id']) if 'id' in json_daily_deal else None
        