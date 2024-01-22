from utils.funciones import cargar_modelo_y_codificador, predecir_nuevos_datos, predecir_nuevos_datos_ordenado
import pandas as pd
from fastapi import APIRouter

#Rutas de los archivos guardados
modelo_guardado = 'data/modelo_svm.pkl'
codificador_etiquetas_guardado = 'data/codificador_etiquetas.pkl'
archivo_embedding = 'data/word_embeddings.p'
data = pd.read_csv('data/turisticov3.csv',
                   delimiter=';', names=["REGION", "TURISTICO"])

turistico = APIRouter()

@turistico.get("/turistico")
async def obtener_turistico():
    #Modelo
    modelo_cargado, codificador_cargado, word_embeddings = cargar_modelo_y_codificador(modelo_guardado, codificador_etiquetas_guardado, archivo_embedding)
    #Seleccionar aleatoriamente un valor de la columna "TURISTICO"
    valor_aleatorio = data["TURISTICO"].sample().iloc[0]
    #Asignar el valor aleatorio a la variable nuevos_datos_texto
    nuevos_datos_texto = [valor_aleatorio]
    #Predicción de los nuevos datos
    resultados = predecir_nuevos_datos(modelo_cargado, codificador_cargado, word_embeddings, nuevos_datos_texto[0])

    return resultados

@turistico.get("/turistico_estruc")
async def obtener_turistico_estruc():
    #Modelo
    modelo_cargado, codificador_cargado, word_embeddings = cargar_modelo_y_codificador(modelo_guardado, codificador_etiquetas_guardado, archivo_embedding)
    #Seleccionar aleatoriamente un valor de la columna "TURISTICO"
    valor_aleatorio = data["TURISTICO"].sample().iloc[0]
    #Asignar el valor aleatorio a la variable nuevos_datos_texto
    nuevos_datos_texto = [valor_aleatorio]
    #Predicción de los nuevos datos
    resultados = predecir_nuevos_datos_ordenado(modelo_cargado, codificador_cargado, word_embeddings, nuevos_datos_texto[0])

    return resultados
