from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session
from db import create_all_tables
from db import getSession
from datetime import date
from models import Player, Performance, Team, League, TeamPlayer

import crud, schemas


app = FastAPI(lifespan=create_all_tables)

@app.get('/')
async def root():
    return{'message':'API conectada correctamente con el servidor'}

@app.get("/v0/players/",response_model=list[schemas.Player], tags=['Players'])
async def read_players(skip: int = 0,
                       limit: int = 100,
                       minimum_last_changed_date: date = None,
                       first_name: str = None,
                       last_name: str = None,
                       db: Session = Depends(getSession)):
    players = crud.get_players(db,
                               skip = skip,
                               limit = limit,
                               min_last_changed_date=minimum_last_changed_date,
                               first_name = first_name,
                               last_name = last_name)
    return players

@app.get("/v0/players/{player_id}", response_model=schemas.Player, tags=['Players'])
async def read_player(player_id: int,
                      db: Session = Depends(getSession)):
    
    player = crud.get_player_by_id(db,
                                   player_id=player_id)
    
    if player is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail='Player Not Found')
    
    return player

@app.get("/v0/performances/",response_model=list[schemas.Performance], tags=['Performance'])
async def read_performances(skip: int = 0,
                       limit: int = 100,
                       minimum_last_changed_date: date = None,
                       db: Session = Depends(getSession)):
    performances = crud.get_performances(db,
                               skip = skip,
                               limit = limit,
                               min_last_changed_date=minimum_last_changed_date)
    return performances

@app.get("/v0/leagues/{league_id}",response_model=schemas.League,tags=['League'])
async def read_league(league_id:int, db:Session = Depends(getSession)):
    league = crud.get_league(db, league_id=league_id)

    if league is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='League not found')
    
    return league

@app.get("/v0/leagues/",response_model=list[schemas.League], tags=['League'])
async def read_leagues(skip: int = 0,
                       limit: int = 100,
                       minimum_last_changed_date: date = None,
                       league_name: str = None,
                       db: Session = Depends(getSession)):
    
    leagues = crud.get_leagues(db,
                               skip = skip,
                               limit = limit,
                               min_last_changed_date=minimum_last_changed_date,
                               league_name=league_name)
    return leagues

@app.get("/v0/teams/",response_model=list[schemas.Team], tags=['teams'])
async def read_leagues(skip: int = 0,
                       limit: int = 100,
                       minimum_last_changed_date: date = None,
                       team_name: str = None,
                       league_id: int = None,
                       db: Session = Depends(getSession)):
    
    teams = crud.get_teams(db,
                           skip = skip,
                           limit = limit,
                           min_last_changed_date=minimum_last_changed_date,
                           team_name= team_name,
                           league_id= league_id)
    return teams

@app.get("/v0/counts/", response_model=schemas.Counts,tags=['Counts'])
def get_count(db: Session = Depends(getSession)):
    counts = schemas.Counts(
        league_count = crud.get_league_count(db),
        team_count = crud.get_team_count(db),
        player_count = crud.get_player_count(db))
    return counts