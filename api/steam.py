from flask import Blueprint, request
import requests

steam_bp = Blueprint('steam_bp', __name__)

@steam_bp.route('/steam/GetPlayerSummaries/')
def GetPlayerSummaries():
    key = request.args.get('key')
    # FOCUS: steamids
    steamids = request.args.get('steamids')
    api_url = "https://community.steam-api.com/ISteamUser/GetPlayerSummaries/v2/"
    response = requests.get(api_url, params={ 'key': key, 'steamids': steamids })
    return response.json(), 200

@steam_bp.route('/steam/GetRecentlyPlayedGames/')
def GetRecentlyPlayedGames():
    key = request.args.get('key')
    steamid = request.args.get('steamid')
    api_url = "https://community.steam-api.com/IPlayerService/GetRecentlyPlayedGames/v1/"
    response = requests.get(api_url, params={ 'key': key, 'steamid': steamid })
    return response.json(), 200

@steam_bp.route('/steam/GetOwnedGames/')
def GetOwnedGames():
    key = request.args.get('key')
    steamid = request.args.get('steamid')
    include_appinfo = request.args.get('include_appinfo')
    api_url = "https://community.steam-api.com/IPlayerService/GetOwnedGames/v1/"
    response = requests.get(api_url, params={ 'key': key, 'steamid': steamid, 'include_appinfo': include_appinfo })
    return response.json(), 200
