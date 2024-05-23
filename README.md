# Análisis de emociones en textos
## Descripción
Este proyecto tiene como objetivo analizar emociones en textos y clasificar cada comentario en cinco categorías, las categorías son "Muy Negativo", "Negativo", "Neutro", "Positivo" y "Muy positivo", de esta forma se puede hacer uso de la clafisicación para seleccionar comentarios para cierto proposito y dependiendo del un tema en específico. En el caso del proyecto, se da la función para clasificar los comentarios en tres categorías, estas son "Comentarios positivos", "Comentarios neutrales" y "Comentarios negativos", además, otra función para generar un comentario aleatorio en la caja de texto para que el usuario lo pueda enviar para analizar y la posibilidad de que el usuario pueda escribir cualquier tipo de texto. Finalmente, este proyecto se realizó en dos partes, la primera parte fue el desarrollo del backend, se usó python junto con el framework FastAPI; la segunda parte fue el desarrollo del frontend, se usaron tecnologías como HTML, CSS, JavaScript, JQuery y Ajax.  
## Instrucciones de uso
Para hacer uso del proyecto, se debe clonar este repositorio de GitHub con el link: [https://github.com/Santiago1470/Analisis-de-emociones-en-texto.git](https://github.com/Santiago1470/Analisis-de-emociones-en-texto.git)  
Antes de ejecutar y usar el proyecto con las páginas web, debe asegurarse de tener instalado Python en su máquina (Se recomienda tener instalada la versión 3.12.3 de Python, esto se debe a que el desarrollo de este proyecto se hizo en base a esa versión).  
Nota: Para la realización de los siguientes pasos, se recomienda estar en la ruta principal del proyecto clonado, en este caso, la ruta debe terminar con `/Analisis-de-emociones-en-text`.  
1. (Opcional/Windows): Activar las políticas de ejecución de Scripts con: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` (Se ejecuta en el powerShell de Visual Studio Code, una vez se cierra el proyecto, la política se restablecerá)

   (Opcional/MacOS): Activamos las políticas de ejecución de Scripts con: `chmod +x script.sh`

2. Creamos un entorno virtual de Python para la instalación de dependencias siguiendo los comandos:
  - Ejecutamos en nuestra terminal `pip install virtualenv`.
  - Creamos el entorno virtual en la terminal `python -m virtualenv analisis-textos`.
  - Iniciamos el entorno virtual `analisis-textos\Scripts\activate`, en el caso de MacOS usamos `source analisis-textos/bin/activate`.

3. Con el entorno virtual, procedemos a instalar las dependencias descritas en `requirements.txt`, se debe usar el comando en la terminal: `pip install -r requirements.txt`

4. Una vez que se hayan instalado las librerías necesarias en el proyecto, ejecutaremos el proyecto con el siguiente comando: `uvicorn main:app --port 3000 --reload` (el puerto puede ser el de su preferencia).

5. Con el servidor de uvicorn iniciado, iremos a la URL: `http://127.0.0.1:3000` (tenga en cuenta el puerto seleccionado en el paso 4).

## Tecnologías usadas

- HTML, CSS y Bootstrap para la maquetación, diseño y decoración de la página web
- JavaScript para capturar los eventos provocados por el usuario
- JQuery para un manejo más rápido y simplificado de componentes del DOM
- Ajax para lograr hacer peticiones a la API de forma asincrónica, es decir, en segundo plano
- Python para la estructuración de todo el código y la base del framework.
- FastAPI para el backend y la construcción de endpoints.
- Uvicorn se usó para el despliegue del servidor en un puerto local.
- TensorFlow para la creación del modelo IA y la carga del mismo en el proyecto.
- NLTK para tokenizar textos largos, dividiéndolos en unidades más pequeñas como palabras o frases, facilitando así el análisis y procesamiento del lenguaje natural.

## Autores

* Andrés Felipe Patarroyo Muñoz  
* Santiago Jair Torres Rivera
