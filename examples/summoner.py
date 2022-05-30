from lol_api import LeagueAPI, Server

# Replace <API-KEY> with your own key
api = LeagueAPI("<API-KEY>")

# An API call happens when this function is called
summoner = api.get_summoner(server=Server.EUW, name="Victor Bot")

print(
    f"""
Name: {summoner.name}
puuid: {summoner.puuid}
icon: {summoner.profile_icon_id}
"""
)
