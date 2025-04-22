from typing import Annotated
from fastapi import Depends,FastAPI
from sqlmodel import Session, create_engine,SQLModel

sqlite_name = "fantasy_data.db"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def getSession():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(getSession)] #Permite Llamar facilmente a la base de datos