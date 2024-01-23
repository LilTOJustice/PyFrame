from collections import defaultdict
from models.common import WarframeObj

class FlashSale(WarframeObj):
    def __init__(self, json_flash_sale: dict):
        json_flash_sale = defaultdict(lambda : None, json_flash_sale)
        self.item = json_flash_sale['item']
        self.expired = json_flash_sale['expired']
        self.eta = json_flash_sale['eta']
        self.discount = json_flash_sale['discount']
        self.premium_override = json_flash_sale['premiumOverride']
        self.is_popular = json_flash_sale['isPopular']
        self.is_featured = json_flash_sale['isFeatured']