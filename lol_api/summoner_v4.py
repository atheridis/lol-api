from dataclasses import dataclass


@dataclass(frozen=True)
class Summoner:
    id: str
    account_id: str
    puuid: str
    name: str
    profile_icon_id: int
    revision_date: int
    summoner_level: int

    @classmethod
    def from_dict(cls, data: dict) -> "Summoner":
        return cls(
            id=data["id"],
            account_id=data["accountId"],
            puuid=data["puuid"],
            name=data["name"],
            profile_icon_id=data["profileIconId"],
            revision_date=data["revisionDate"],
            summoner_level=data["summonerLevel"],
        )
