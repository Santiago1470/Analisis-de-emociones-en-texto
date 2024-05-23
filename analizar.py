from transformers import pipeline
# from transformers import BertTokenizer
from nltk.tokenize import sent_tokenize

# python -m nltk.downloader all

clasificador = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

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
    
