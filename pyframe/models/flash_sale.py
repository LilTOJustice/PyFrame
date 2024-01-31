from pyframe.models.common import WarframeObj

class FlashSale(WarframeObj):
    def __init__(self, json_flash_sale: dict):
        self.item = str(json_flash_sale['item']) if 'item' in json_flash_sale else None
        self.expired = str(json_flash_sale['expired']) if 'expired' in json_flash_sale else None
        self.eta = str(json_flash_sale['eta']) if 'eta' in json_flash_sale else None
        self.discount = int(json_flash_sale['discount']) if 'discount' in json_flash_sale else None
        self.premium_override = int(json_flash_sale['premiumOverride']) if 'premiumOverride' in json_flash_sale else None
        self.is_popular = bool(json_flash_sale['isPopular']) if 'isPopular' in json_flash_sale else None
        self.is_featured = bool(json_flash_sale['isFeatured']) if 'isFeatured' in json_flash_sale else None