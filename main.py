from fastapi import FastAPI
import pandas as pd
from routers import turisticos, players, comidas 

#Rutas de los archivos guardados
# modelo_guardado = 'data/modelo_svm.pkl'
# codificador_etiquetas_guardado = 'data/codificador_etiquetas.pkl'
# archivo_embedding = 'data/word_embeddings.p'
# data = pd.read_csv('data/turisticov3.csv',
#                    delimiter=';', names=["REGION", "TURISTICO"])

# class Player(BaseModel):
#     id: int
#     nickname: str
#     score: int

# jugadores = [Player(id=1, nickname = "david", score =2300)]

# def buscarPlayer(nickname: str):
#     players = filter(lambda player: player.nickname == nickname, jugadores)
#     try:
#         return list(players)[0]
#     except:
#         return {"error": "Player no encontrado"}

    
app = FastAPI()

app.include_router(turisticos.turistico)
app.include_router(comidas.comida)
app.include_router(players.player)

@app.get("/")
async def root():
 return "Hola, ¡si funcinona la API!"
