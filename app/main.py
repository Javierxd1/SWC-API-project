from fastapi import FastAPI, Depends
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