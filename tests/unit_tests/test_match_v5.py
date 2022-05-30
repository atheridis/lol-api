from lol_api.match_v5.match_data import Match
from lol_api.match_v5.match_timeline import EventType, MatchTimeline, Position


def test_match_v5(match_data_info) -> None:
    match = Match.from_dict(match_data_info)
    assert isinstance(match, Match)


def test_match_v5_match_id(match_data_info) -> None:
    match = Match.from_dict(match_data_info)
    assert match.metadata.match_id == "EUW1_5895423846"


def test_match_v5_timeline(match_timeline_info) -> None:
    match_timeline = MatchTimeline.from_dict(match_timeline_info)
    assert isinstance(match_timeline, MatchTimeline)


def test_match_v5_timeline_match_id(match_timeline_info) -> None:
    match_timeline = MatchTimeline.from_dict(match_timeline_info)
    assert match_timeline.metadata.match_id == "EUW1_5895423846"


def test_match_v5_timeline_champion_kill(match_timeline_info) -> None:
    match_timeline = MatchTimeline.from_dict(match_timeline_info)
    event = match_timeline.info.frames[2].events[14]
    if isinstance(event, EventType.CHAMPION_KILL.value):
        assert event.position == Position(6701, 6713)
    else:
        assert False
