from fastapi import FastAPI
from db import create_all_tables
from db import SessionDep
from models import Player, Performance, Team, League, TeamPlayer

import crud, schemas


app = FastAPI(lifespan=create_all_tables)

@app.get('/')
async def root():
    return{'message':'API conectada correctamente con el servidor'}

@app.get("/v0/players/{player_id}",response_model=list[schemas.Player])