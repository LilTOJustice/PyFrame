from collections import defaultdict
from pyframe.models.alert import Alert
from pyframe.models.arbitration import Arbitration
from pyframe.models.archon_hunt import ArchonHunt
from pyframe.models.cambion_cycle import CambionCycle
from pyframe.models.cetus_cycle import CetusCycle
from pyframe.models.conclave_challenge import ConclaveChallenge
from pyframe.models.construction_progress import ConstructionProgress
from pyframe.models.daily_deal import DailyDeal
from pyframe.models.dark_sector import DarkSector
from pyframe.models.earth_cycle import EarthCycle
from pyframe.models.event import Event
from pyframe.models.fissure import Fissure
from pyframe.models.flash_sale import FlashSale
from pyframe.models.global_upgrade import GlobalUpgrade
from pyframe.models.invasion import Invasion
from pyframe.models.kuva import Kuva
from pyframe.models.common import WarframeObj
from pyframe.models.news import News
from pyframe.models.nightwave import Nightwave
from pyframe.models.persistent_enemy import PersistentEnemy
from pyframe.models.simaris import Simaris
from pyframe.models.sortie import Sortie
from pyframe.models.steel_path import SteelPath
from pyframe.models.syndicate_mission import SyndicateMission
from pyframe.models.vallis_cycle import VallisCycle
from pyframe.models.void_trader import VoidTrader

class Worldstate(WarframeObj):
    def __init__(self, json_worldstate: dict):
        json_worldstate = defaultdict(lambda : None, json_worldstate)
        self.timestamp = json_worldstate['timestamp']
        self.alerts = [Alert(alert) for alert in json_worldstate['alerts']] if 'alerts' in json_worldstate else []
        self.arbitration = Arbitration(json_worldstate['arbitration']) if 'arbitration' in json_worldstate else None
        self.archon_hunt = ArchonHunt(json_worldstate['archonHunt']) if 'archonHunt' in json_worldstate else None
        self.cambion_cycle = CambionCycle(json_worldstate['cambionCycle']) if 'cambionCycle' in json_worldstate else None
        self.cetus_cycle = CetusCycle(json_worldstate['cetusCycle']) if 'cetusCycle' in json_worldstate else None
        self.conclave_challenges = [ConclaveChallenge(conclave_challenge) for conclave_challenge in json_worldstate['conclaveChallenges']] if 'conclaveChallenges' in json_worldstate else []
        self.construction_progress = ConstructionProgress(json_worldstate['constructionProgress']) if 'constructionProgress' in json_worldstate else None
        self.daily_deals = [DailyDeal(daily_deal) for daily_deal in json_worldstate['dailyDeals']] if 'dailyDeals' in json_worldstate else []
        self.dark_sectors = [DarkSector(dark_sector) for dark_sector in json_worldstate['darkSectors']] if 'darkSectors' in json_worldstate else []
        self.earth_cycle = EarthCycle(json_worldstate['earthCycle']) if 'earthCycle' in json_worldstate else None
        self.events = [Event(event) for event in json_worldstate['events']] if 'events' in json_worldstate else []
        self.fissures = [Fissure(fissure) for fissure in json_worldstate['fissures']] if 'fissures' in json_worldstate else []
        self.flash_sales = [FlashSale(flash_sale) for flash_sale in json_worldstate['flashSales']] if 'flashSales' in json_worldstate else []
        self.global_upgrades = [GlobalUpgrade(global_upgrade) for global_upgrade in json_worldstate['globalUpgrades']] if 'globalUpgrades' in json_worldstate else []
        self.invasions = [Invasion(invasion) for invasion in json_worldstate['invasions']] if 'invasions' in json_worldstate else []
        self.kuva = [Kuva(kuva) for kuva in json_worldstate['kuva']] if 'kuva' in json_worldstate else []
        self.news = [News(news) for news in json_worldstate['news']] if 'news' in json_worldstate else []
        self.nightwave = Nightwave(json_worldstate['nightwave']) if 'nightwave' in json_worldstate else None
        self.persistent_enemies = [PersistentEnemy(persistent_enemy) for persistent_enemy in json_worldstate['persistentEnemies']] if 'persistentEnemies' in json_worldstate else []
        self.simaris = Simaris(json_worldstate['simaris']) if 'simaris' in json_worldstate else None
        self.sortie = Sortie(json_worldstate['sortie']) if 'sortie' in json_worldstate else None
        self.steel_path = SteelPath(json_worldstate['steelPath']) if 'steelPath' in json_worldstate else None
        self.syndicate_missions = [SyndicateMission(syndicate_mission) for syndicate_mission in json_worldstate['syndicateMissions']] if 'syndicateMissions' in json_worldstate else []
        self.vallis_cycle = VallisCycle(json_worldstate['vallisCycle']) if 'vallisCycle' in json_worldstate else None
        self.void_trader = VoidTrader(json_worldstate['voidTrader']) if 'voidTrader' in json_worldstate else None