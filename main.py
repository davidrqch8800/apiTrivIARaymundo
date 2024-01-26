from fastapi import FastAPI
import pandas as pd
from routers import turisticos, players, comidas 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(turisticos.turistico)
app.include_router(comidas.comida)
app.include_router(players.player)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
 return "Hola, ¡si funcinona la API!"
