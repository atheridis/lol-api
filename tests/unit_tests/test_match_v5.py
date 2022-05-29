from lol_api.match_v5 import Match


def test_match_v5(match_data_info) -> None:
    match = Match.from_dict(match_data_info)
    assert isinstance(match, Match)


def test_match_v5_match_id(match_data_info) -> None:
    match = Match.from_dict(match_data_info)
    assert match.metadata.match_id == "EUW1_5895423846"
