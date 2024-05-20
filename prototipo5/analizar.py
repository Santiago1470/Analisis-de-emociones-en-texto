from transformers import pipeline
clasificador = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

def analizar_sentimiento_hf(texto):
    resultado = clasificador(texto)
    return resultado, resultado[0]['label']

# texto = "bueno"
# resultado = analizar_sentimiento_hf(texto)
# print(resultado)