from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    @classmethod
    def from_dict(cls, data: dict) -> "Position":
        return cls(
            x=data["x"],
            y=data["y"],
        )


@dataclass(frozen=True)
class VictimDamage:
    basic: bool
    magic_damage: int
    name: str
    participant_id: int
    physical_damage: int
    spell_name: str
    spell_slot: int
    true_damage: int
    type: str

    @classmethod
    def from_dict(cls, data: dict) -> "VictimDamage":
        return cls(
            basic=data["basic"],
            magic_damage=data["magicDamage"],
            name=data["name"],
            participant_id=data["participantId"],
            physical_damage=data["physicalDamage"],
            spell_name=data["spellName"],
            spell_slot=data["spellSlot"],
            true_damage=data["trueDamage"],
            type=data["type"],
        )


class BuildingType(Enum):
    TOWER_BUILDING = "TOWER_BUILDING"
    INHIBITOR_BUILDING = "INHIBITOR_BUILDING"


class TowerType(Enum):
    INNER_TURRET = "INNER_TURRET"
    BASE_TURRET = "BASE_TURRET"
    OUTER_TURRET = "OUTER_TURRET"
    NEXUS_TURRET = "NEXUS_TURRET"


class LaneType(Enum):
    MID_LANE = "MID_LANE"
    TOP_LANE = "TOP_LANE"
    BOT_LANE = "BOT_LANE"


class LevelUpType(Enum):
    NORMAL = "NORMAL"
    EVOLVE = "EVOLVE"


class WardType(Enum):
    YELLOW_TRINKET = "YELLOW_TRINKET"
    BLUE_TRINKET = "BLUE_TRINKET"
    SIGHT_WARD = "SIGHT_WARD"
    CONTROL_WARD = "CONTROL_WARD"
    TEEMO_MUSHROOM = "TEEMO_MUSHROOM"
    UNDEFINED = "UNDEFINED"


class KillType(Enum):
    KILL_FIRST_BLOOD = "KILL_FIRST_BLOOD"
    KILL_MULTI = "KILL_MULTI"
    KILL_ACE = "KILL_ACE"


class MonsterType(Enum):
    DRAGON = "DRAGON"
    BARON_NASHOR = "BARON_NASHOR"
    RIFTHERALD = "RIFTHERALD"


class MonsterSubType(Enum):
    EARTH_DRAGON = "EARTH_DRAGON"
    AIR_DRAGON = "AIR_DRAGON"
    HEXTECH_DRAGON = "HEXTECH_DRAGON"
    WATER_DRAGON = "WATER_DRAGON"
    FIRE_DRAGON = "FIRE_DRAGON"


class DragonSoulGivenType(Enum):
    Mountain = "Mountain"
    Cloud = "Cloud"
    Hextech = "Hextech"
    Ocean = "Ocean"
    Infernal = "Infernal"


class ChampionTransformType(Enum):
    ASSASSIN = "ASSASSIN"
    SLAYER = "SLAYER"


@dataclass(frozen=True)
class Participants:
    participant_id: int
    puuid: str

    @classmethod
    def from_dict(cls, data: dict) -> "Participants":
        return cls(
            participant_id=data["participantId"],
            puuid=data["puuid"],
        )


@dataclass(frozen=True)
class Event:
    timestamp: int
    type: str

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return cls(
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class GameEnd(Event):
    game_id: int
    real_timestamp: int
    winning_team: int

    @classmethod
    def from_dict(cls, data: dict) -> "GameEnd":
        return cls(
            game_id=data["gameId"],
            real_timestamp=data["realTimestamp"],
            winning_team=data["winningTeam"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ItemSold(Event):
    item_id: int
    participant_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "ItemSold":
        return cls(
            item_id=data["itemId"],
            participant_id=data["participantId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ItemPurchased(Event):
    item_id: int
    participant_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "ItemPurchased":
        return cls(
            item_id=data["itemId"],
            participant_id=data["participantId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ItemDestroyed(Event):
    item_id: int
    participant_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "ItemDestroyed":
        return cls(
            item_id=data["itemId"],
            participant_id=data["participantId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ItemUndo(Event):
    after_id: int
    before_id: int
    gold_gain: int
    participant_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "ItemUndo":
        return cls(
            after_id=data["afterId"],
            before_id=data["beforeId"],
            gold_gain=data["goldGain"],
            participant_id=data["participantId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class PauseEnd(Event):
    real_timestamp: int

    @classmethod
    def from_dict(cls, data: dict) -> "PauseEnd":
        return cls(
            real_timestamp=data["realTimestamp"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class LevelUp(Event):
    level: int
    participant_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "LevelUp":
        return cls(
            level=data["level"],
            participant_id=data["participantId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class SkillLevelUp(Event):
    level_up_type: LevelUpType
    participant_id: int
    skill_slot: int

    @classmethod
    def from_dict(cls, data: dict) -> "SkillLevelUp":
        level_up_type = LevelUpType[data["levelUpType"]]
        return cls(
            level_up_type=level_up_type,
            participant_id=data["participantId"],
            skill_slot=data["skillSlot"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class WardPlaced(Event):
    creator_id: int
    ward_type: WardType

    @classmethod
    def from_dict(cls, data: dict) -> "WardPlaced":
        ward_type = WardType[data["wardType"]]
        return cls(
            creator_id=data["creatorId"],
            ward_type=ward_type,
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class WardKill(Event):
    killer_id: int
    ward_type: WardType

    @classmethod
    def from_dict(cls, data: dict) -> "WardKill":
        ward_type = WardType[data["wardType"]]
        return cls(
            killer_id=data["killerId"],
            ward_type=ward_type,
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ChampionKill(Event):
    assisting_participant_ids: list[int]
    bounty: int
    kill_streak_length: int
    killer_id: int
    position: Position
    shutdown_bounty: int
    victim_damage_dealt: list[VictimDamage]
    victim_damage_received: list[VictimDamage]
    victim_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "ChampionKill":
        position = Position.from_dict(data["position"])
        victim_damage_received = [
            VictimDamage.from_dict(x) for x in data["victimDamageReceived"]
        ]
        victim_damage_dealt = [
            VictimDamage.from_dict(x) for x in data.get("victimDamageDealt", [])
        ]
        return cls(
            assisting_participant_ids=data.get("assistingParticipantIds", []),
            bounty=data["bounty"],
            kill_streak_length=data["killStreakLength"],
            killer_id=data["killerId"],
            position=position,
            shutdown_bounty=data["shutdownBounty"],
            victim_damage_dealt=victim_damage_dealt,
            victim_damage_received=victim_damage_received,
            victim_id=data["victimId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ChampionSpecialKill(Event):
    kill_type: KillType
    killer_id: int
    multi_kill_length: Optional[int]
    position: Position

    @classmethod
    def from_dict(cls, data: dict) -> "ChampionSpecialKill":
        position = Position.from_dict(data["position"])
        kill_type = KillType[data["killType"]]
        return cls(
            kill_type=kill_type,
            killer_id=data["killerId"],
            multi_kill_length=data.get("multiKillLength", None),
            position=position,
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class BuildingKill(Event):
    assisting_participant_ids: list[int]
    bounty: int
    building_type: BuildingType
    killer_id: int
    lane_type: LaneType
    position: Position
    team_id: int
    tower_type: Optional[TowerType]

    @classmethod
    def from_dict(cls, data: dict) -> "BuildingKill":
        position = Position.from_dict(data["position"])
        building_type = BuildingType[data["buildingType"]]
        lane_type = LaneType[data["laneType"]]
        try:
            tower_type = TowerType[data["towerType"]]
        except KeyError:
            tower_type = None
        return cls(
            assisting_participant_ids=data.get("assistingParticipantIds", []),
            bounty=data["bounty"],
            building_type=building_type,
            killer_id=data["killerId"],
            lane_type=lane_type,
            position=position,
            team_id=data["teamId"],
            tower_type=tower_type,
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class TurretPlateDestroyed(Event):
    killer_id: int
    lane_type: LaneType
    position: Position
    team_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "TurretPlateDestroyed":
        position = Position.from_dict(data["position"])
        lane_type = LaneType[data["laneType"]]
        return cls(
            killer_id=data["killerId"],
            lane_type=lane_type,
            position=position,
            team_id=data["teamId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ObjectiveBountyPrestart(Event):
    actual_start_time: int
    team_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "ObjectiveBountyPrestart":
        return cls(
            actual_start_time=data["actualStartTime"],
            team_id=data["teamId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ObjectiveBountyFinish(Event):
    team_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "ObjectiveBountyFinish":
        return cls(
            team_id=data["teamId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class EliteMonsterKill(Event):
    assisting_participant_ids: list[int]
    bounty: int
    killer_id: int
    killer_team_id: int
    monster_sub_type: Optional[MonsterSubType]
    monster_type: MonsterType
    position: Position

    @classmethod
    def from_dict(cls, data: dict) -> "EliteMonsterKill":
        monster_type = MonsterType[data["monsterType"]]
        try:
            monster_sub_type = MonsterSubType[data["monsterSubType"]]
        except KeyError:
            monster_sub_type = None
        position = Position.from_dict(data["position"])
        return cls(
            assisting_participant_ids=data.get("assistingParticipantIds", []),
            bounty=data["bounty"],
            killer_id=data["killerId"],
            killer_team_id=data["killerTeamId"],
            monster_sub_type=monster_sub_type,
            monster_type=monster_type,
            position=position,
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class DragonSoulGiven(Event):
    name: DragonSoulGivenType
    team_id: int

    @classmethod
    def from_dict(cls, data: dict) -> "DragonSoulGiven":
        name = DragonSoulGivenType[data["name"]]
        return cls(
            name=name,
            team_id=data["teamId"],
            timestamp=data["timestamp"],
            type=data["type"],
        )


@dataclass(frozen=True)
class ChampionTransform(Event):
    participant_id: int
    transform_type: ChampionTransformType

    @classmethod
    def from_dict(cls, data: dict) -> "ChampionTransform":
        transform_type = ChampionTransformType[data["transform_type"]]
        return cls(
            participant_id=data["participantId"],
            transform_type=transform_type,
            timestamp=data["timestamp"],
            type=data["type"],
        )


class EventType(Enum):
    ITEM_UNDO = ItemUndo
    ITEM_SOLD = ItemSold
    ITEM_PURCHASED = ItemPurchased
    ITEM_DESTROYED = ItemDestroyed
    PAUSE_END = PauseEnd
    LEVEL_UP = LevelUp
    SKILL_LEVEL_UP = SkillLevelUp
    WARD_PLACED = WardPlaced
    WARD_KILL = WardKill
    ELITE_MONSTER_KILL = EliteMonsterKill
    DRAGON_SOUL_GIVEN = DragonSoulGiven
    CHAMPION_KILL = ChampionKill
    CHAMPION_SPECIAL_KILL = ChampionSpecialKill
    BUILDING_KILL = BuildingKill
    TURRET_PLATE_DESTROYED = TurretPlateDestroyed
    OBJECTIVE_BOUNTY_PRESTART = ObjectiveBountyPrestart
    OBJECTIVE_BOUNTY_FINISH = ObjectiveBountyFinish
    CHAMPION_TRANSFORM = ChampionTransform
    GAME_END = GameEnd
    UNDEFINED = Event

    @classmethod
    def check(cls, x) -> "EventType":
        for k in cls:
            if type(x) == k.value:
                return k
        return cls.UNDEFINED

    @staticmethod
    def create_event_from_data(data: dict) -> Event:
        data_type = data["type"]
        try:
            return EventType[data_type].value.from_dict(data)
        except KeyError:
            return EventType["UNDEFINED"].value.from_dict(data)


@dataclass(frozen=True)
class ChampionStats:
    ability_haste: int
    ability_power: int
    armor: int
    armor_pen: int
    armor_pen_percent: int
    attack_damage: int
    attack_speed: int
    bonus_armor_pen_percent: int
    bonus_magic_pen_percent: int
    cc_reduction: int
    cooldown_reduction: int
    health: int
    health_max: int
    health_regen: int
    lifesteal: int
    magic_pen: int
    magic_pen_percent: int
    magic_resist: int
    movement_speed: int
    omnivamp: int
    physical_vamp: int
    power: int
    power_max: int
    power_regen: int
    spell_vamp: int

    @classmethod
    def from_dict(cls, data: dict) -> "ChampionStats":
        return cls(
            ability_haste=data["abilityHaste"],
            ability_power=data["abilityPower"],
            armor=data["armor"],
            armor_pen=data["armorPen"],
            armor_pen_percent=data["armorPenPercent"],
            attack_damage=data["attackDamage"],
            attack_speed=data["attackSpeed"],
            bonus_armor_pen_percent=data["bonusArmorPenPercent"],
            bonus_magic_pen_percent=data["bonusMagicPenPercent"],
            cc_reduction=data["ccReduction"],
            cooldown_reduction=data["cooldownReduction"],
            health=data["health"],
            health_max=data["healthMax"],
            health_regen=data["healthRegen"],
            lifesteal=data["lifesteal"],
            magic_pen=data["magicPen"],
            magic_pen_percent=data["magicPenPercent"],
            magic_resist=data["magicResist"],
            movement_speed=data["movementSpeed"],
            omnivamp=data["omnivamp"],
            physical_vamp=data["physicalVamp"],
            power=data["power"],
            power_max=data["powerMax"],
            power_regen=data["powerRegen"],
            spell_vamp=data["spellVamp"],
        )


@dataclass(frozen=True)
class DamageStats:
    magic_damage_done: int
    magic_damage_done_to_champions: int
    magic_damage_taken: int
    physical_damage_done: int
    physical_damage_done_to_champions: int
    physical_damage_taken: int
    total_damage_done: int
    total_damage_done_to_champions: int
    total_damage_taken: int
    true_damage_done: int
    true_damage_done_to_champions: int
    true_damage_taken: int

    @classmethod
    def from_dict(cls, data: dict) -> "DamageStats":
        return cls(
            magic_damage_done=data["magicDamageDone"],
            magic_damage_done_to_champions=data["magicDamageDoneToChampions"],
            magic_damage_taken=data["magicDamageTaken"],
            physical_damage_done=data["physicalDamageDone"],
            physical_damage_done_to_champions=data["physicalDamageDoneToChampions"],
            physical_damage_taken=data["physicalDamageTaken"],
            total_damage_done=data["totalDamageDone"],
            total_damage_done_to_champions=data["totalDamageDoneToChampions"],
            total_damage_taken=data["totalDamageTaken"],
            true_damage_done=data["trueDamageDone"],
            true_damage_done_to_champions=data["trueDamageDoneToChampions"],
            true_damage_taken=data["trueDamageTaken"],
        )


@dataclass(frozen=True)
class ParticipantFrame:
    champion_stats: ChampionStats
    current_gold: int
    damage_stats: DamageStats
    gold_per_second: int
    jungle_minions_killed: int
    level: int
    minions_killed: int
    participant_id: int
    position: Position
    time_enemy_spent_controlled: int
    total_gold: int
    xp: int

    @classmethod
    def from_dict(cls, data: dict) -> "ParticipantFrame":
        damage_stats = DamageStats.from_dict(data["damageStats"])
        champion_stats = ChampionStats.from_dict(data["championStats"])
        return cls(
            champion_stats=champion_stats,
            current_gold=data["currentGold"],
            damage_stats=damage_stats,
            gold_per_second=data["goldPerSecond"],
            jungle_minions_killed=data["jungleMinionsKilled"],
            level=data["level"],
            minions_killed=data["minionsKilled"],
            participant_id=data["participantId"],
            position=data["position"],
            time_enemy_spent_controlled=data["timeEnemySpentControlled"],
            total_gold=data["totalGold"],
            xp=data["xp"],
        )


@dataclass(frozen=True)
class Frame:
    events: list[Event]
    participant_frames: dict[int, ParticipantFrame]
    timestamp: int

    @classmethod
    def from_dict(cls, data: dict) -> "Frame":
        participant_frames = {}
        for k, v in data["participantFrames"].items():
            participant_frames[int(k)] = ParticipantFrame.from_dict(v)
        events = [EventType.create_event_from_data(x) for x in data["events"]]
        return cls(
            events=events,
            participant_frames=participant_frames,
            timestamp=data["timestamp"],
        )


@dataclass(frozen=True)
class Info:
    frame_interval: int
    frames: list[Frame]
    game_id: int
    participants: list[Participants]

    @classmethod
    def from_dict(cls, data: dict) -> "Info":
        participants = [Participants.from_dict(x) for x in data["participants"]]
        frames = [Frame.from_dict(x) for x in data["frames"]]
        return cls(
            frame_interval=data["frameInterval"],
            frames=frames,
            game_id=data["gameId"],
            participants=participants,
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
class MatchTimeline:
    metadata: Metadata
    info: Info

    @classmethod
    def from_dict(cls, data: dict) -> "MatchTimeline":
        metadata = Metadata.from_dict(data["metadata"])
        info = Info.from_dict(data["info"])
        return cls(
            metadata=metadata,
            info=info,
        )
