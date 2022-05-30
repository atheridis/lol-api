from typing import Optional, Union
from urllib.parse import urljoin

import requests

from .lol_exceptions import LoLException, NotFoundException
from .match_v5.match_data import Match
from .match_v5.match_timeline import MatchTimeline
from .servers import Server
from .summoner_v4 import Summoner


class LeagueAPI:
    def __init__(self, key: str):
        self.key = key
        self.header = {"X-Riot-Token": key}

    def _base_request(
        self,
        endpoint: str,
        server: Server,
        region: bool = False,
        **kwargs,
    ) -> Union[list, dict]:
        base_url = f"https://{server.value[region]}.api.riotgames.com"
        params = {}
        for k in kwargs:
            if kwargs[k]:
                params[k] = kwargs[k]
        response = requests.get(
            urljoin(base_url, endpoint),
            params=params,
            headers=self.header,
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise NotFoundException()
        else:
            raise LoLException()

    def get_summoner(
        self,
        server: Server,
        name: Optional[str] = None,
        puuid: Optional[str] = None,
        account_id: Optional[str] = None,
        summoner_id: Optional[str] = None,
    ) -> Summoner:
        if name:
            endpoint = f"/lol/summoner/v4/summoners/by-name/{name}"
        elif puuid:
            endpoint = f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
        elif account_id:
            endpoint = f"/lol/summoner/v4/summoners/by-puuid/{account_id}"
        elif summoner_id:
            endpoint = f"/lol/summoner/v4/summoners/by-puuid/{summoner_id}"
        else:
            raise LoLException()

        response = self._base_request(endpoint, server)
        if not isinstance(response, dict):
            raise LoLException()
        return Summoner.from_dict(response)

    def get_match_history(
        self,
        server: Server,
        puuid: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        queue: Optional[int] = None,
        type: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
    ) -> list[str]:
        endpoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
        response = self._base_request(
            endpoint=endpoint,
            server=server,
            region=True,
            startTime=start_time,
            endTime=end_time,
            queue=queue,
            type=type,
            start=start,
            count=count,
        )
        if not isinstance(response, list):
            raise LoLException()
        return response

    def get_match_data(
        self,
        server: Server,
        match_id: str,
    ) -> Match:
        endpoint = f"/lol/match/v5/matches/{match_id}"
        response = self._base_request(endpoint=endpoint, server=server, region=True)
        if not isinstance(response, dict):
            raise LoLException()
        return Match.from_dict(response)

    def get_match_timeline(
        self,
        server: Server,
        match_id: str,
    ) -> MatchTimeline:
        endpoint = f"/lol/match/v5/matches/{match_id}/timeline"
        response = self._base_request(endpoint=endpoint, server=server, region=True)
        if not isinstance(response, dict):
            raise LoLException()
        return MatchTimeline.from_dict(response)
