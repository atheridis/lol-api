from unittest.mock import Mock, patch

import pytest
from lol_api import LeagueAPI, Server
from lol_api.lol_exceptions import LoLException, NotFoundException
from lol_api.match_v5 import Match, Metadata
from lol_api.summoner_v4 import Summoner


@patch("lol_api.lol_api.requests.get")
def test_summoner_ok_by_name(mock_get, summoner_v4_info) -> None:
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = summoner_v4_info
    api = LeagueAPI("example-key")
    summoner = api.get_summoner(Server.EUW, name=summoner_v4_info["name"])
    assert isinstance(summoner, Summoner)


@patch("lol_api.lol_api.requests.get")
def test_summoner_ok_by_puuid(mock_get, summoner_v4_info) -> None:
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = summoner_v4_info
    api = LeagueAPI("example-key")
    summoner = api.get_summoner(Server.EUW, puuid=summoner_v4_info["puuid"])
    assert isinstance(summoner, Summoner)


@patch("lol_api.lol_api.requests.get")
def test_summoner_ok_by_summoner_id(mock_get, summoner_v4_info) -> None:
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = summoner_v4_info
    api = LeagueAPI("example-key")
    summoner = api.get_summoner(Server.EUW, summoner_id=summoner_v4_info["id"])
    assert isinstance(summoner, Summoner)


@patch("lol_api.lol_api.requests.get")
def test_summoner_ok_by_account_id(mock_get, summoner_v4_info) -> None:
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = summoner_v4_info
    api = LeagueAPI("example-key")
    summoner = api.get_summoner(Server.EUW, account_id=summoner_v4_info["accountId"])
    assert isinstance(summoner, Summoner)


@patch("lol_api.lol_api.requests.get")
def test_summoner_not_found(mock_get) -> None:
    mock_get.return_value = Mock(status_code=404)
    api = LeagueAPI("example-key")
    with pytest.raises(NotFoundException):
        api.get_summoner(Server.BR, "y")


def test_summoner_no_input() -> None:
    api = LeagueAPI("example-key")
    with pytest.raises(LoLException):
        api.get_summoner(Server.BR)


@patch("lol_api.lol_api.requests.get")
def test_match_history_ok(mock_get, match_history_info) -> None:
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = match_history_info
    api = LeagueAPI("example-key")
    match_history = api.get_match_history(Server.EUW, "puuid")
    assert isinstance(match_history, list)


@patch("lol_api.lol_api.requests.get")
def test_match_history_not_found(mock_get) -> None:
    mock_get.return_value = Mock(status_code=404)
    api = LeagueAPI("example-key")
    with pytest.raises(NotFoundException):
        api.get_match_history(Server.BR, "e")


@patch("lol_api.lol_api.requests.get")
def test_match_data_ok(mock_get, match_data_info) -> None:
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = match_data_info
    api = LeagueAPI("example-key")
    match_data = api.get_match_data(Server.EUW, "match_id")
    assert isinstance(match_data, Match)
    assert isinstance(match_data.metadata, Metadata)
