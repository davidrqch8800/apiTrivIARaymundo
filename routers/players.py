from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated, List
from models import models
from config.dbp import engine, SessionLocal
from sqlalchemy.orm import Session

player = APIRouter()
models.Base.metadata.create_all(bind=engine)

class Player(BaseModel):
    nickname: str
    score: int

class UserBase(BaseModel):
    nickname: str
    score: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

db_dependency = Annotated[Session, Depends(get_db)]

# @player.get("/players")
# async def players():
#     return ["players aqui"]

@player.get("/player/{player_id}", status_code=status.HTTP_200_OK)
async def mostrar_player(player_id: int, db: db_dependency):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if player is None:
        raise HTTPException(status_code=404, detail='Player no encontrado')
    return player

@player.get("/playersDesc", status_code=status.HTTP_200_OK)
async def mostrar_players_descendente(db: Session = Depends(get_db)):
    players = db.query(models.Player).order_by(models.Player.score.desc()).all()
    return players

@player.post("/player/", status_code=status.HTTP_201_CREATED)
async def ingresar_player(player: UserBase, db: db_dependency):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()

@player.delete("/player/{player_id}", status_code=status.HTTP_200_OK)
async def eliminar_player(player_id: int, db: db_dependency):
    db_player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail='Player no encontrado')
    db.delete(db_player)
    db.commit()
