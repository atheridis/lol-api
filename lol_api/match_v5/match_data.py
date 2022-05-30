from dataclasses import dataclass


@dataclass(frozen=True)
class Matchdata:
    data_version: str
    match_id: str
    participants: list[str]

    @classmethod
    def from_dict(cls, data: dict) -> "Matchdata":
        return cls(
            data_version=data["dataVersion"],
            match_id=data["matchId"],
            participants=data["partcipants"],
        )


@dataclass(frozen=True)
class PerkStat:
    defense: int
    flex: int
    offense: int

    @classmethod
    def from_dict(cls, data: dict) -> "PerkStat":
        return cls(
            defense=data["defense"],
            flex=data["flex"],
            offense=data["offense"],
        )


@dataclass(frozen=True)
class PerkStyleSelection:
    perk: int
    var_1: int
    var_2: int
    var_3: int

    @classmethod
    def from_dict(cls, data: dict) -> "PerkStyleSelection":
        return cls(
            perk=data["perk"],
            var_1=data["var1"],
            var_2=data["var2"],
            var_3=data["var3"],
        )


@dataclass(frozen=True)
class PerkStyle:
    description: str
    selections: list[PerkStyleSelection]
    style: int

    @classmethod
    def from_dict(cls, data: dict) -> "PerkStyle":
        selections = [PerkStyleSelection.from_dict(x) for x in data["selections"]]
        return cls(
            description=data["description"],
            selections=selections,
            style=data["style"],
        )


@dataclass(frozen=True)
class Perks:
    stat_perks: PerkStat
    styles: list[PerkStyle]

    @classmethod
    def from_dict(cls, data: dict) -> "Perks":
        stat_perks = PerkStat.from_dict(data["statPerks"])
        styles = [PerkStyle.from_dict(x) for x in data["styles"]]
        return cls(
            stat_perks=stat_perks,
            styles=styles,
        )


@dataclass(frozen=True)
class Participants:
    assists: int
    baron_kills: int
    bounty_level: int
    champ_experience: int
    champ_level: int
    champion_id: int
    champion_name: str
    champion_transform: int
    consumables_purchased: int
    damage_dealt_to_buildings: int
    damage_dealt_to_objectives: int
    damage_dealt_to_turrets: int
    damage_self_mitigated: int
    deaths: int
    detector_wards_placed: int
    double_kills: int
    dragon_kills: int
    first_blood_assist: bool
    first_blood_kill: bool
    first_tower_assist: bool
    first_tower_kill: bool
    game_ended_in_early_surrender: bool
    game_ended_in_surrender: bool
    gold_earned: int
    gold_spent: int
    individual_position: str
    inhibitor_kills: int
    inhibitor_takedowns: int
    inhibitors_lost: int
    item_0: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    item_6: int
    items_purchased: int
    killing_sprees: int
    kills: int
    lane: str
    largest_critical_strike: int
    largest_killing_spree: int
    largest_multi_kill: int
    longest_time_spent_living: int
    magic_damage_dealt: int
    magic_damage_dealt_to_champions: int
    magic_damage_taken: int
    neutral_minions_killed: int
    nexus_kills: int
    nexus_takedowns: int
    nexus_lost: int
    objectives_stolen: int
    objectives_stolen_assists: int
    participant_id: int
    penta_kills: int
    perks: Perks
    physical_damage_dealt: int
    physical_damage_dealt_to_champions: int
    physical_damage_taken: int
    profile_icon: int
    puuid: str
    quadra_kills: int
    riot_id_name: str
    riot_id_tagline: str
    role: str
    sight_wards_bought_in_game: int
    spell_1_casts: int
    spell_2_casts: int
    spell_3_casts: int
    spell_4_casts: int
    summoner_1_casts: int
    summoner_1_id: int
    summoner_2_casts: int
    summoner_2_id: int
    summoner_id: str
    summoner_level: int
    summoner_name: str
    team_early_surrendered: bool
    team_id: int
    team_position: str
    time_ccing_others: int
    time_played: int
    total_damage_dealt: int
    total_damage_dealt_to_champions: int
    total_damage_shielded_on_teammates: int
    total_damage_taken: int
    total_heal: int
    total_heals_on_teammates: int
    total_minions_killed: int
    total_time_cc_dealt: int
    total_time_spent_dead: int
    total_units_healed: int
    triple_kills: int
    true_damage_dealt: int
    true_damage_dealt_to_champions: int
    true_damage_taken: int
    turret_kills: int
    turret_takedowns: int
    turrets_lost: int
    unreal_kills: int
    vision_score: int
    vision_wards_bought_in_game: int
    wards_killed: int
    wards_placed: int
    win: bool

    @classmethod
    def from_dict(cls, data: dict) -> "Participants":
        perks = Perks.from_dict(data["perks"])
        return cls(
            assists=data["assists"],
            baron_kills=data["baronKills"],
            bounty_level=data["bountyLevel"],
            champ_experience=data["champExperience"],
            champ_level=data["champLevel"],
            champion_id=data["championId"],
            champion_name=data["championName"],
            champion_transform=data["championTransform"],
            consumables_purchased=data["consumablesPurchased"],
            damage_dealt_to_buildings=data["damageDealtToBuildings"],
            damage_dealt_to_objectives=data["damageDealtToObjectives"],
            damage_dealt_to_turrets=data["damageDealtToTurrets"],
            damage_self_mitigated=data["damageSelfMitigated"],
            deaths=data["deaths"],
            detector_wards_placed=data["detectorWardsPlaced"],
            double_kills=data["doubleKills"],
            dragon_kills=data["dragonKills"],
            first_blood_assist=data["firstBloodAssist"],
            first_blood_kill=data["firstBloodKill"],
            first_tower_assist=data["firstTowerAssist"],
            first_tower_kill=data["firstTowerKill"],
            game_ended_in_early_surrender=data["gameEndedInEarlySurrender"],
            game_ended_in_surrender=data["gameEndedInSurrender"],
            gold_earned=data["goldEarned"],
            gold_spent=data["goldSpent"],
            individual_position=data["individualPosition"],
            inhibitor_kills=data["inhibitorKills"],
            inhibitor_takedowns=data["inhibitorTakedowns"],
            inhibitors_lost=data["inhibitorsLost"],
            item_0=data["item0"],
            item_1=data["item1"],
            item_2=data["item2"],
            item_3=data["item3"],
            item_4=data["item4"],
            item_5=data["item5"],
            item_6=data["item6"],
            items_purchased=data["itemsPurchased"],
            killing_sprees=data["killingSprees"],
            kills=data["kills"],
            lane=data["lane"],
            largest_critical_strike=data["largestCriticalStrike"],
            largest_killing_spree=data["largestKillingSpree"],
            largest_multi_kill=data["largestMultiKill"],
            longest_time_spent_living=data["longestTimeSpentLiving"],
            magic_damage_dealt=data["magicDamageDealt"],
            magic_damage_dealt_to_champions=data["magicDamageDealtToChampions"],
            magic_damage_taken=data["magicDamageTaken"],
            neutral_minions_killed=data["neutralMinionsKilled"],
            nexus_kills=data["nexusKills"],
            nexus_takedowns=data["nexusTakedowns"],
            nexus_lost=data["nexusLost"],
            objectives_stolen=data["objectivesStolen"],
            objectives_stolen_assists=data["objectivesStolenAssists"],
            participant_id=data["participantId"],
            penta_kills=data["pentaKills"],
            perks=perks,
            physical_damage_dealt=data["physicalDamageDealt"],
            physical_damage_dealt_to_champions=data["physicalDamageDealtToChampions"],
            physical_damage_taken=data["physicalDamageTaken"],
            profile_icon=data["profileIcon"],
            puuid=data["puuid"],
            quadra_kills=data["quadraKills"],
            riot_id_name=data["riotIdName"],
            riot_id_tagline=data["riotIdTagline"],
            role=data["role"],
            sight_wards_bought_in_game=data["sightWardsBoughtInGame"],
            spell_1_casts=data["spell1Casts"],
            spell_2_casts=data["spell2Casts"],
            spell_3_casts=data["spell3Casts"],
            spell_4_casts=data["spell4Casts"],
            summoner_1_casts=data["summoner1Casts"],
            summoner_1_id=data["summoner1Id"],
            summoner_2_casts=data["summoner2Casts"],
            summoner_2_id=data["summoner2Id"],
            summoner_id=data["summonerId"],
            summoner_level=data["summonerLevel"],
            summoner_name=data["summonerName"],
            team_early_surrendered=data["teamEarlySurrendered"],
            team_id=data["teamId"],
            team_position=data["teamPosition"],
            time_ccing_others=data["timeCCingOthers"],
            time_played=data["timePlayed"],
            total_damage_dealt=data["totalDamageDealt"],
            total_damage_dealt_to_champions=data["totalDamageDealtToChampions"],
            total_damage_shielded_on_teammates=data["totalDamageShieldedOnTeammates"],
            total_damage_taken=data["totalDamageTaken"],
            total_heal=data["totalHeal"],
            total_heals_on_teammates=data["totalHealsOnTeammates"],
            total_minions_killed=data["totalMinionsKilled"],
            total_time_cc_dealt=data["totalTimeCCDealt"],
            total_time_spent_dead=data["totalTimeSpentDead"],
            total_units_healed=data["totalUnitsHealed"],
            triple_kills=data["tripleKills"],
            true_damage_dealt=data["trueDamageDealt"],
            true_damage_dealt_to_champions=data["trueDamageDealtToChampions"],
            true_damage_taken=data["trueDamageTaken"],
            turret_kills=data["turretKills"],
            turret_takedowns=data["turretTakedowns"],
            turrets_lost=data["turretsLost"],
            unreal_kills=data["unrealKills"],
            vision_score=data["visionScore"],
            vision_wards_bought_in_game=data["visionWardsBoughtInGame"],
            wards_killed=data["wardsKilled"],
            wards_placed=data["wardsPlaced"],
            win=data["win"],
        )


@dataclass(frozen=True)
class Objective:
    first: bool
    kills: int

    @classmethod
    def from_dict(cls, data: dict) -> "Objective":
        return cls(
            first=data["first"],
            kills=data["kills"],
        )


@dataclass(frozen=True)
class Objectives:
    baron: Objective
    champion: Objective
    dragon: Objective
    inhibitor: Objective
    rift_herald: Objective
    tower: Objective

    @classmethod
    def from_dict(cls, data: dict) -> "Objectives":
        baron = Objective.from_dict(data["baron"])
        champion = Objective.from_dict(data["champion"])
        dragon = Objective.from_dict(data["dragon"])
        inhibitor = Objective.from_dict(data["inhibitor"])
        rift_herald = Objective.from_dict(data["riftHerald"])
        tower = Objective.from_dict(data["tower"])
        return cls(
            baron=baron,
            champion=champion,
            dragon=dragon,
            inhibitor=inhibitor,
            rift_herald=rift_herald,
            tower=tower,
        )


@dataclass(frozen=True)
class Ban:
    champion_id: int
    pick_turn: int

    @classmethod
    def from_dict(cls, data: dict) -> "Ban":
        return cls(
            champion_id=data["championId"],
            pick_turn=data["pickTurn"],
        )


@dataclass(frozen=True)
class Team:
    bans: list[Ban]
    objectives: Objectives
    team_id: int
    win: bool

    @classmethod
    def from_dict(cls, data: dict) -> "Team":
        bans = [Ban.from_dict(x) for x in data["bans"]]
        objectives = Objectives.from_dict(data["objectives"])
        return cls(
            bans=bans,
            objectives=objectives,
            team_id=data["teamId"],
            win=data["win"],
        )


@dataclass(frozen=True)
class Info:
    game_creation: int
    game_duration: int
    game_end_timestamp: int
    game_id: int
    game_mode: str
    game_name: str
    game_start_timestamp: int
    game_type: str
    game_version: str
    map_id: int
    participants: list[Participants]
    platform_id: str
    queue_id: int
    teams: list[Team]
    tournament_code: str

    @classmethod
    def from_dict(cls, data: dict) -> "Info":
        participants = [Participants.from_dict(x) for x in data["participants"]]
        teams = [Team.from_dict(x) for x in data["teams"]]
        return cls(
            game_creation=data["gameCreation"],
            game_duration=data["gameDuration"],
            game_end_timestamp=data["gameEndTimestamp"],
            game_id=data["gameId"],
            game_mode=data["gameMode"],
            game_name=data["gameName"],
            game_start_timestamp=data["gameStartTimestamp"],
            game_type=data["gameType"],
            game_version=data["gameVersion"],
            map_id=data["mapId"],
            participants=participants,
            platform_id=data["platformId"],
            queue_id=data["queueId"],
            teams=teams,
            tournament_code=data["tournamentCode"],
        )


@dataclass(frozen=True)
class Metadata:
    data_version: str
    match_id: str
    participants: list[str]

    @classmethod
    def from_dict(cls, data: dict) -> "Metadata":
        return cls(
            data_version=data["dataVersion"],
            match_id=data["matchId"],
            participants=data["participants"],
        )


@dataclass(frozen=True)
class Match:
    metadata: Metadata
    info: Info

    @classmethod
    def from_dict(cls, data: dict) -> "Match":
        metadata = Metadata.from_dict(data["metadata"])
        info = Info.from_dict(data["info"])
        return cls(
            metadata=metadata,
            info=info,
        )
