import json

import pytest


@pytest.fixture
def summoner_v4_info():
    """Fixture that returns static summoner_v4 data."""
    with open("tests/resources/summoner-v4.json") as f:
        return json.load(f)


@pytest.fixture
def match_history_info():
    """Fixture that returns static match_history data in list format."""
    with open("tests/resources/match-v5.json") as f:
        return json.load(f)["match-history"]


@pytest.fixture
def match_data_info():
    """Fixture that returns static match_history data in list format."""
    with open("tests/resources/match-v5.json") as f:
        return json.load(f)["match-data"]


@pytest.fixture
def match_timeline_info():
    """Fixture that returns static match_history data in list format."""
    with open("tests/resources/match-v5.json") as f:
        return json.load(f)["match-timeline"]
