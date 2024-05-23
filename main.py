from fastapi import FastAPI, Query
from analizar import analizar_sentimiento_hf
from clasificacion import stars, tipo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from textoInput import TextoInput
import json
import random

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analizarTexto")
def emotionsText_detect(texto_input: TextoInput):
    texto = texto_input.texto
    resultado = analizar_sentimiento_hf(texto)
    print(resultado)
    # print(resultado[1])
    emocion = stars[resultado[1]]
    # stars = resultado[1]
    # stars = resultado[stars]
    return {"Servicio": "El comentario analizado es " + emocion}


@app.get("/comentarioAleatorio")
def buscarComentario_aleatorio():
    with open('comentarios.json', 'r', encoding='utf-8') as file:
        datos = json.load(file)
    comentarios = datos['comentarios']
    comentario = random.choice(comentarios)
    return {"Comentario": comentario}

# @app.get("/comentarios")
# def buscarComentarios():
#     with open('comentarios.json', 'r', encoding='utf-8') as file:
#         datos = json.load(file)
#     comentarios = datos['comentarios']
#     return {"Comentario": comentarios}

@app.get("/comentarios")
def buscar_comentarios(tipoComentario: str = Query(..., description="Tipo de comentario: positivo, neutral o negativo")):
    with open('comentarios.json', 'r', encoding='utf-8') as file:
        datos = json.load(file)
    comentarios = datos['comentarios']
    # print(comentarios)
    emociones = []
    for c in comentarios:
        resultado = analizar_sentimiento_hf(c['comentario'])
        
        if (stars[resultado[1]] == 'Positivo' or stars[resultado[1]] == 'Muy Positivo') and (tipoComentario == 'positivo'):
            print(resultado)
            emociones.append(c)
        elif stars[resultado[1]] == 'Neutro' and (tipoComentario == 'neutral'):
            emociones.append(c)
        elif (stars[resultado[1]] == 'Negativo' or stars[resultado[1]] == 'Muy Negativo') and (tipoComentario == 'negativo'):
            emociones.append(c)
    
    return {"Comentario": emociones}
