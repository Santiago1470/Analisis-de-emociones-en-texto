from transformers import pipeline
# from transformers import BertTokenizer
from nltk.tokenize import sent_tokenize

# python -m nltk.downloader all

clasificador = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# def analizar_emociones_texto(texto, segment_size=512):
#     # Dividir el texto en segmentos
#     segmentos = [texto[i:i+segment_size] for i in range(0, len(texto), segment_size)]
    
#     # Analizar emociones para cada segmento
#     resultados_segmentos = []
#     for segmento in segmentos:
#         resultado_segmento = clasificador(segmento)
#         resultados_segmentos.append(resultado_segmento)
    
#     return resultados_segmentos


def analizar_sentimiento_hf(texto):
    sentences = sent_tokenize(texto)
    # print(sentences)
    resultado = clasificador(sentences)
    # print(resultado)
    prom = 0
    for i in range(len(resultado)):
        prom += resultado[i]['score']
    prom = prom / len(resultado)
    # print(prom)
    resultado[len(resultado) - 1]['score'] = prom
    # print(resultado[len(resultado) - 1]['score'])
    return resultado, resultado[len(resultado) - 1]['label']

# def analizar_sentimiento_hf(texto):
#     resultado = clasificador(texto)
#     return resultado, resultado[0]['label']

# texto = "bueno"
# resultado = analizar_sentimiento_hf(texto)
# print(resultado)