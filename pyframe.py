import requests
from models.alert import Alert
from models.arbitration import Arbitration
from models.archon_hunt import ArchonHunt
from models.event import Event
from models.conclave_challenge import ConclaveChallenge
from models.cambion_cycle import CambionCycle
from models.cetus_cycle import CetusCycle
from models.construction_progress import ConstructionProgress
from models.daily_deal import DailyDeal
from models.earth_cycle import EarthCycle
from models.fissure import Fissure
from models.flash_sale import FlashSale
from models.global_upgrade import GlobalUpgrade
from models.news import News
from models.sortie import Sortie
from models.steel_path import SteelPath
from models.persistent_enemy import PersistentEnemy

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

def get_events(platform: str = "pc") -> list[Event]:
    return [Event(event) for event in get(platform, "events")]

def get_conclave_challenges(platform: str = "pc") -> ConclaveChallenge:
    return [ConclaveChallenge(conclave_challenge) for conclave_challenge in get(platform, "conclaveChallenges")]

def get_cambion_cycle(platform: str = "pc") -> CambionCycle:
    return CambionCycle(get(platform, "cambionCycle"))

def get_cetus_cycle(platform: str = "pc") -> CetusCycle:
    return CetusCycle(get(platform, "cetusCycle"))

def get_construction_progress(platform: str = "pc") -> ConstructionProgress:
    return ConstructionProgress(get(platform, "constructionProgress"))

def get_daily_deals(platform: str = "pc") -> list[DailyDeal]:
    return [DailyDeal(deal) for deal in get(platform, "dailyDeals")]

def get_earth_cycle(platform: str = "pc") -> EarthCycle:
    return EarthCycle(get(platform, "earthCycle"))

def get_fissures(platform: str = "pc") -> list[Fissure]:
    return [Fissure(fissure) for fissure in get(platform, "fissures")]

def get_global_upgrades(platform: str = "pc") -> list[GlobalUpgrade]:
    return [GlobalUpgrade(upgrade) for upgrade in get(platform, "globalUpgrades")]

def get_news(platform: str = "pc") -> list[News]:
    return [News(news) for news in get(platform, "news")]

def get_sortie(platform: str = "pc") -> list[Sortie]:
    return Sortie(get(platform, "sortie"))

def get_steel_path(platform: str = "pc") -> SteelPath:
    return SteelPath(get(platform, "steelPath"))

def get_flash_sales(platform: str = "pc") -> list[FlashSale]:
    return [FlashSale(flash_sale) for flash_sale in get(platform, "flashSales")]

def get_persistent_enemy(platform: str = "pc") -> list[PersistentEnemy]:
    return [PersistentEnemy(persistent_enemy) for persistent_enemy in get(platform, "persistentEnemies")]

if __name__ == "__main__":
    print("Alerts:")
    print(get_alerts())
    print("\nArbitration:")
    print(get_arbitration())
    print("\nArchon Hunt:")
    print(get_archon_hunt())
    print("\nEvents:")
    print(get_events())
    print("\nConclave Challenge:")
    print(get_conclave_challenges())
    print("\nCambion Cycle:")
    print(get_cambion_cycle())
    print("\nCetus Cycle:")
    print(get_cetus_cycle())
    print("\nConstruction Progress:")
    print(get_construction_progress())
    print("\nDaily Deals:")
    print(get_daily_deals())
    print("\nNews")
    print(get_news())
    print("\nGlobal Upgrades:")
    print(get_global_upgrades())
    print("\nSortie:")
    print(get_sortie())
    print("\nSteel Path") 
    print(get_steel_path())
    print("\nFlash Sales:")
    print(get_flash_sales())
    print("\nPersistent Enemy")
    print(get_persistent_enemy())