from collections import defaultdict
import requests
from models.alert import Alert
from models.arbitration import Arbitration
from models.archon_hunt import ArchonHunt
from models.conclave_challenge import ConclaveChallenge

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

def get_conclave_challenges(platform: str = "pc") -> ConclaveChallenge:
    return [ConclaveChallenge(conclave_challenge) for conclave_challenge in get(platform, "conclaveChallenges")]

if __name__ == "__main__":
    print("Alerts:")
    print(get_alerts())
    print("\nArbitration:")
    print(get_arbitration())
    print("\nArchon Hunt:")
    print(get_archon_hunt())
    print("\nConclave Challenge")
    print(get_conclave_challenges())