from fastapi import FastAPI
from analizar import analizar_sentimiento_hf
from stars import clasificacion
from fastapi.middleware.cors import CORSMiddleware
from textoInput import TextoInput

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Aplicación": "Correindo"}

@app.post("/analizarTexto")
def emotionsText_detect(texto_input: TextoInput):
    texto = texto_input.texto
    resultado = analizar_sentimiento_hf(texto)
    print(resultado)
    stars = resultado[1]
    stars = clasificacion[stars]
    return {"Servicio": "El comentario analizado es " + stars}