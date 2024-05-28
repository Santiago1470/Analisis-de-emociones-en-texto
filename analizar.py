from transformers import pipeline
# from transformers import BertTokenizer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# python -m nltk.downloader all
nltk.download("punkt")

clasificador = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

def analizar_sentimiento_hf(texto):
    if len(word_tokenize(texto)) > 500:
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
    else:
        resultado = clasificador(texto)
    return resultado, resultado[len(resultado) - 1]['label']
    
