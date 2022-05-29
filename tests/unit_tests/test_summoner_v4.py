from lol_api.summoner_v4 import Summoner


def test_summoner_v4(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert isinstance(summoner, Summoner)


def test_summoner_v4_name(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert summoner.name == "MagiFelix5"


def test_summoner_v4_puuid(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert len(summoner.puuid) == 78
    assert isinstance(summoner.puuid, str)


def test_summoner_v4_id(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert len(summoner.id) == 47
    assert isinstance(summoner.id, str)


def test_summoner_v4_account_id(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert len(summoner.account_id) == 46
    assert isinstance(summoner.account_id, str)


def test_summoner_v4_level(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert summoner.summoner_level == 467


def test_summoner_v4_profile_icon_id(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert summoner.profile_icon_id == 548


def test_summoner_v4_revision_date(summoner_v4_info) -> None:
    summoner = Summoner.from_dict(summoner_v4_info)
    assert isinstance(summoner.revision_date, int)
