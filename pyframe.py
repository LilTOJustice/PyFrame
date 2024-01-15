from collections import defaultdict
import requests
from models.alert import Alert
from models.arbitration import Arbitration
from models.archon_hunt import ArchonHunt
from models.cetus_cycle import CetusCycle
from models.daily_deal import DailyDeal
from models.earth_cycle import EarthCycle
from models.fissure import Fissure
from models.global_upgrade import GlobalUpgrade
from models.news import News

class APIException(Exception):
    pass

def get(platform: str, route: str) -> dict | list[dict]:
    response = requests.get(f"https://api.warframestat.us/{platform}/{route}")
    if response.status_code != 200:
        raise APIException(f"Call to route '{route}' on platform '{platform}' failed.")
    return response.json()

def get_alerts(platform: str = "pc") -> list[Alert]:
    return [Alert(alert) for alert in get(platform, "alerts")]

def get_arbitration(platform: str = "pc") -> Arbitration:
    return Arbitration(get(platform, "arbitration"))

def get_archon_hunt(platform: str = "pc") -> ArchonHunt:
    return ArchonHunt(get(platform, "archonHunt"))

def get_cetus_cycle(platform: str = "pc") -> CetusCycle:
    return CetusCycle(get(platform, "cetusCycle"))

def get_daily_deals(platform: str = "pc") -> list[DailyDeal]:
    return [DailyDeal(deal) for deal in get(platform, "dailyDeals")]

def get_earth_cycle(platform: str = "pc") -> EarthCycle:
    return EarthCycle(get(platform, "earthCycle"))

def get_fissures(platform: str = "pc") -> list[Fissure]:
    return [Fissure(fissure) for fissure in get(platform, "fissures")]

def get_global_upgrade(platform: str = "pc") -> list[GlobalUpgrade]:
    return [GlobalUpgrade(upgrade) for upgrade in get(platform, "globalUpgrades")]

def get_news(platform: str = "pc") -> list[News]:
    return [News(news) for news in get(platform, "news")]

if __name__ == "__main__":
    print("Alerts:")
    print(get_alerts())
    print("\nArbitration:")
    print(get_arbitration())
    print("\nArchon Hunt:")
    print(get_archon_hunt())
    print("\nCetus Cycle")
    print(get_cetus_cycle())
    print("\nDaily Deals")
    print(get_daily_deals())
    print("\nGlobal Upgrades")
    print(get_global_upgrade())
    print("\nNews")
    print(get_news())