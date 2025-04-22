from datetime import date
from typing import Optional, List

from sqlmodel import Session, select
from sqlalchemy.orm import selectinload 

from models import Player, Performance, League, Team
from sqlalchemy import func


def get_player_by_id(db: Session,
                     player_id: int) -> List[Player]:
    
    statement = (select(Player).where(Player.player_id == player_id))
    return db.exec(statement).first()

def get_players(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    min_last_changed_date: Optional[date] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None):

    statement = select(Player)

    if min_last_changed_date is not None:
        statement = statement.where(
            Player.last_changed_date >= min_last_changed_date
        )

    if first_name is not None:
        statement = statement.where(
            Player.first_name == first_name
        )

    if last_name is not None:
        statement = statement.where(
            Player.last_name == last_name
        )

    statement = statement.offset(skip).limit(limit)
    return db.exec(statement).all()

def get_performances(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    min_last_changed_date: Optional[date] = None) -> List[Performance]:

    statement = select(Performance)

    if min_last_changed_date is not None:
        statement = statement.where(
            Performance.last_changed_date >= min_last_changed_date
        )

    statement = statement.offset(skip).limit(limit)
    return db.exec(statement).all()

def get_league(db:Session,
               league_id: int):
    
    statement = select(League).where(League.league_id == league_id)
    return db.exec(statement).first()

def get_leagues(db:Session,
                skip: int = 0,
                limit: int = 100,
                min_last_changed_date: date = None,
                league_name: str = None) -> List[League]:
    
    statement = select(League).options(selectinload(League.teams))

    if min_last_changed_date is not None:
        statement = statement.where(
            League.last_changed_date >= min_last_changed_date
        )
    
    if league_name is not None:
        statement = statement.where(
            League.league_name == league_name
        )
    
    statement = statement.offset(skip).limit(limit)

    return db.exec(statement).all()

def get_teams(db:Session,
                skip: int = 0,
                limit: int = 100,
                min_last_changed_date: date = None,
                team_name: str = None,
                league_id: int = None )-> List[Team]:
    
    statement = select(Team)

    if min_last_changed_date is not None:
        statement = statement.where(
            Team.last_changed_date >= min_last_changed_date
        )
    
    if team_name is not None:
        statement = statement.where(
            Team.team_name == team_name
        )
    
    if league_id is not None:
        statement = statement.where(
            Team.league_id == league_id
        )
    
    statement = statement.offset(skip).limit(limit)

    return db.exec(statement).all()

##Analytics Queries
def get_player_count(db:Session) -> int:
    statement = select(func.count(Player.player_id))
    return db.exec(statement).scalar_one()

def get_team_count(db:Session) -> int:
    statement = select(func.count(Team.team_id))
    return db.exec(statement).scalar_one()

def get_league_count(db:Session) -> int:
    statement = select(func.count(League.league_id))
    return db.exec(statement).scalar_one()