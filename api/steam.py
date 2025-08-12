from flask import Blueprint, request
import requests

steam_bp = Blueprint('steam_bp', __name__)

@steam_bp.route('/steam/GetPlayerSummaries/')
def GetPlayerSummaries():
    key = request.args.get('key')
    steamids = request.args.get('steamids')
    api_url = "https://community.steam-api.com/ISteamUser/GetPlayerSummaries/v2/"
    r = requests.get(api_url, params={ 'key': key, 'steamids': steamids })
    return r.json()

