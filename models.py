from typing import Optional, List
from datetime import date
from sqlmodel import SQLModel, Field, Relationship


class TeamPlayer(SQLModel, table=True):
    team_id: Optional[int] = Field(default=None, foreign_key="team.team_id", primary_key=True)
    player_id: Optional[int] = Field(default=None, foreign_key="player.player_id", primary_key=True)
    last_changed_date: date


class Player(SQLModel, table=True):
    player_id: Optional[int] = Field(default=None, primary_key=True)
    gsis_id: str
    first_name: str
    last_name: str
    position: str
    last_changed_date: date

    performances: List["Performance"] = Relationship(back_populates="player")
    teams: List["Team"] = Relationship(back_populates="players", link_model=TeamPlayer)


class Performance(SQLModel, table=True):
    performance_id: Optional[int] = Field(default=None, primary_key=True)
    week_number: str
    fantasy_points: float
    player_id: int = Field(foreign_key="player.player_id")
    last_changed_date: date

    player: Optional[Player] = Relationship(back_populates="performances")


class League(SQLModel, table=True):
    league_id: Optional[int] = Field(default=None, primary_key=True)
    league_name: str
    scoring_type: str
    last_changed_date: date

    teams: List["Team"] = Relationship(back_populates="league")


class Team(SQLModel, table=True):
    team_id: Optional[int] = Field(default=None, primary_key=True)
    team_name: str
    league_id: Optional[int] = Field(default=None, foreign_key="league.league_id")
    last_changed_date: date

    league: Optional[League] = Relationship(back_populates="teams")
    players: List[Player] = Relationship(back_populates="teams", link_model=TeamPlayer)
