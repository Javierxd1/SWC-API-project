from fastapi import FastAPI
#from db import create_all_tables
#from models import Player, Performance, Team, League, TeamPlayer


app = FastAPI()

@app.get('/')
async def root():
    return{'message':'API conectada correctamente con el servidor'}