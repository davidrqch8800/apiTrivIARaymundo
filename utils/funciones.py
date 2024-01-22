import numpy as np
import pickle

def cargar_modelo_y_codificador(modelo_ruta, codificador_ruta, embedding_ruta):
    modelo = pickle.load(open(modelo_ruta, 'rb'))
    codificador = pickle.load(open(codificador_ruta, 'rb'))
    word_embeddings = pickle.load(open(embedding_ruta, 'rb'))
    return modelo, codificador, word_embeddings

def obtener_embedding_promedio(texto, embeddings):
    palabras = texto.split()
    embeddings_palabras = [embeddings[palabra] for palabra in palabras if palabra in embeddings]

    if embeddings_palabras:
        return np.mean(embeddings_palabras, axis=0)
    else:
        return np.zeros_like(next(iter(embeddings.values())))

def predecir_nuevos_datos(modelo, codificador, word_embeddings, nuevos_datos_texto):
    resultados = np.empty((4, 2), dtype=object)

    nuevos_datos_embedding = obtener_embedding_promedio(nuevos_datos_texto, word_embeddings)

    #Obtener las probabilidades para cada clase en lugar de las predicciones
    prediccion_probabilidad = modelo.predict_proba([nuevos_datos_embedding])

    #Guardar el dato introducido
    resultados[0, 0] = "REGION ALEATORIA"
    resultados[0, 1] = nuevos_datos_texto

    #Obtener las etiquetas de las tres predicciones más precisas
    top3_indices = np.argsort(prediccion_probabilidad, axis=1)[:, ::-1][:, :3]
    top3_labels = codificador.inverse_transform(top3_indices.flatten())

    #Guardar los resultados más precisos y sus porcentajes
    for i in range(3):
        resultados[i + 1, 0] = f"{top3_labels[i]}"
        resultados[i + 1, 1] = f"{prediccion_probabilidad[0, top3_indices.flatten()[i]] * 100:.2f}%"

    return resultados

def predecir_nuevos_datos_ordenado(modelo, codificador, word_embeddings, nuevos_datos_texto):
    resultados = np.empty((7, 2), dtype=object)

    nuevos_datos_embedding = obtener_embedding_promedio(nuevos_datos_texto, word_embeddings)

    #Obtener las probabilidades para cada clase en lugar de las predicciones
    prediccion_probabilidad = modelo.predict_proba([nuevos_datos_embedding])

    #Guardar el dato introducido
    resultados[0, 0] = "REGION ALEATORIA"
    resultados[0, 1] = nuevos_datos_texto
    resultados[1, 0] = "REGION1"
    resultados[2, 0] = "REGION2"
    resultados[3, 0] = "REGION3"
    resultados[4, 0] = "PRESICION1"
    resultados[5, 0] = "PRESICION2"
    resultados[6, 0] = "PRESICION3"


    #Obtener las etiquetas de las tres predicciones más precisas
    top3_indices = np.argsort(prediccion_probabilidad, axis=1)[:, ::-1][:, :3]
    top3_labels = codificador.inverse_transform(top3_indices.flatten())

    #Guardar los resultados más precisos y sus porcentajes
    for i in range(3):
        resultados[i + 1, 1] = f"{top3_labels[i]}" 
        resultados[i + 4, 1] = f"{prediccion_probabilidad[0, top3_indices.flatten()[i]] * 100:.2f}%"

    return resultados


#Mostrar resultados
# for i in range(resultados.shape[0]):
#     print(f'{resultados[i, 0]}: {resultados[i, 1]}')