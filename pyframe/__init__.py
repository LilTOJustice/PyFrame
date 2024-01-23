import requests
from models.alert import Alert
from models.arbitration import Arbitration
from models.archon_hunt import ArchonHunt
from models.conclave_challenge import ConclaveChallenge
from models.cambion_cycle import CambionCycle
from models.cetus_cycle import CetusCycle
from models.construction_progress import ConstructionProgress
from models.daily_deal import DailyDeal
from models.earth_cycle import EarthCycle
from models.event import Event
from models.fissure import Fissure
from models.flash_sale import FlashSale
from models.global_upgrade import GlobalUpgrade
from models.invasion import Invasion
from models.kuva import Kuva
from models.news import News
from models.nightwave import Nightwave
from models.persistent_enemy import PersistentEnemy
from models.simaris import Simaris
from models.sortie import Sortie
from models.steel_path import SteelPath
from models.syndicate_mission import SyndicateMission
from models.vallis_cycle import VallisCycle
from models.void_trader import VoidTrader
from models.worldstate import Worldstate

class APIException(Exception):
    pass

def get(platform: str, route: str) -> dict | list[dict]:
    response = requests.get(f"https://api.warframestat.us/{platform}/{route}")
    if response.status_code != 200:
        raise APIException(f"Call to route '{route}' on platform '{platform}' failed.")
    return response.json()

def get_worldstate(platform: str = "pc") -> Worldstate:
    return Worldstate(get(platform, ""))

def get_alerts(platform: str = "pc") -> list[Alert]:
    return [Alert(alert) for alert in get(platform, "alerts")]

def get_arbitration(platform: str = "pc") -> Arbitration:
    return Arbitration(get(platform, "arbitration"))

def get_archon_hunt(platform: str = "pc") -> ArchonHunt:
    return ArchonHunt(get(platform, "archonHunt"))

def get_cambion_cycle(platform: str = "pc") -> CambionCycle:
    return CambionCycle(get(platform, "cambionCycle"))

def get_cetus_cycle(platform: str = "pc") -> CetusCycle:
    return CetusCycle(get(platform, "cetusCycle"))

def get_conclave_challenges(platform: str = "pc") -> ConclaveChallenge:
    return [ConclaveChallenge(conclave_challenge) for conclave_challenge in get(platform, "conclaveChallenges")]

def get_construction_progress(platform: str = "pc") -> ConstructionProgress:
    return ConstructionProgress(get(platform, "constructionProgress"))

def get_daily_deals(platform: str = "pc") -> list[DailyDeal]:
    return [DailyDeal(deal) for deal in get(platform, "dailyDeals")]

def get_earth_cycle(platform: str = "pc") -> EarthCycle:
    return EarthCycle(get(platform, "earthCycle"))

def get_events(platform: str = "pc") -> list[Event]:
    return [Event(event) for event in get(platform, "events")]

def get_fissures(platform: str = "pc") -> list[Fissure]:
    return [Fissure(fissure) for fissure in get(platform, "fissures")]

def get_flash_sales(platform: str = "pc") -> list[FlashSale]:
    return [FlashSale(flash_sale) for flash_sale in get(platform, "flashSales")]

def get_global_upgrades(platform: str = "pc") -> list[GlobalUpgrade]:
    return [GlobalUpgrade(upgrade) for upgrade in get(platform, "globalUpgrades")]

def get_invasions(platform: str = "pc") -> list[Invasion]:
    return [Invasion(invasion) for invasion in get(platform, "invasions")]

def get_kuva(platform: str = "pc") -> list[Kuva]:
    return [Kuva(kuva) for kuva in get(platform, "kuva")]
    
def get_news(platform: str = "pc") -> list[News]:
    return [News(news) for news in get(platform, "news")]

def get_nightwave(platform: str = "pc") -> Nightwave:
    return Nightwave(get(platform, "nightwave"))

def get_persistent_enemy(platform: str = "pc") -> list[PersistentEnemy]:
    return [PersistentEnemy(persistent_enemy) for persistent_enemy in get(platform, "persistentEnemies")]

def get_simaris(platform: str = "pc") -> Simaris:
    return Simaris(get(platform, "simaris"))

def get_sortie(platform: str = "pc") -> list[Sortie]:
    return Sortie(get(platform, "sortie"))

def get_steel_path(platform: str = "pc") -> SteelPath:
    return SteelPath(get(platform, "steelPath"))

def get_syndicate_mission(platform: str = "pc") -> list[SyndicateMission]:
    return [SyndicateMission(syndicate_mission) for syndicate_mission in get(platform, "syndicateMissions")]

def get_vallis_cycle(platform: str = "pc") -> VallisCycle:
    return VallisCycle(platform, "vallisCycle")

def get_void_trader(platform: str = "pc") -> VoidTrader:
    return VoidTrader(platform, "voidTrader")