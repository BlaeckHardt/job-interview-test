import spacy

# Cargar el modelo en español
nlp = spacy.load("es_core_news_sm")

def procesar_oracion(oracion):
    # Procesar la oración con spaCy
    doc = nlp(oracion)

    # Obtener las entidades nombradas encontradas
    entidades_nombradas = [{entidad.text: entidad.label_} for entidad in doc.ents]
    resultado_final = {k: v for dic in entidades_nombradas for k, v in dic.items()}
    
    return resultado_final

def procesar_lista(lista):
    resultados = []
    for elemento in lista:
        resultado = {}
        resultado["oracion"] = elemento
        resultado["entidades"] = procesar_oracion(elemento)
        resultados.append(resultado)
    
    return resultados


