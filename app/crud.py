from datetime import date
from typing import Optional, List

from sqlmodel import Session, select # type: ignore
from sqlmodel.orm import selectinload # type: ignore

from models import Player, Performance


def get_player_by_id(
    db: Session,
    player_id: int) -> Optional[Player]:
    
    statement = (
        select(Player)
        .where(Player.player_id == player_id)
        .options(
            selectinload(Player.performances),
            selectinload(Player.teams)
        )
    )
    return db.exec(statement).first()


def get_players(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    min_last_changed_date: Optional[date] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None) -> List[Player]:

    statement = select(Player)

    if min_last_changed_date:
        statement = statement.where(
            Player.last_changed_date >= min_last_changed_date
        )

    if first_name:
        statement = statement.where(
            Player.first_name == first_name
        )

    if last_name:
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

    if min_last_changed_date:
        statement = statement.where(
            Performance.last_changed_date >= min_last_changed_date
        )

    statement = statement.offset(skip).limit(limit)
    return db.exec(statement).all()
