# 🤖 Agente Conversacional con LangChain, OpenAI y FastAPI para Facebook Messenger

Este proyecto demuestra cómo construir un chatbot de inteligencia artificial utilizando [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/) y [FastAPI](https://fastapi.tiangolo.com/) integrado con [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/). Aprenderás a configurar webhooks, integrar LangChain con OpenAI y desplegar un agente conversacional funcional que responde a mensajes en tiempo real.

> 🎥 Este repositorio acompaña al video tutorial disponible en [YouTube](https://www.youtube.com/watch?v=UHNEeMXwyoc), donde se explica paso a paso la implementación.

---

## 🧠 Tecnologías Utilizadas

- **LangChain**: Framework para construir aplicaciones de lenguaje natural con modelos de lenguaje grandes (LLMs).
- **OpenAI**: Proveedor de modelos de lenguaje avanzados como GPT-4.
- **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs con Python.
- **Facebook Messenger Platform**: Plataforma de mensajería para interactuar con usuarios a través de bots.

---

## 🚀 Características

- Configuración de webhooks para recibir y enviar mensajes desde y hacia Facebook Messenger.
- Integración con LangChain y OpenAI para generar respuestas inteligentes.
- Implementación de una cadena simple utilizando `model.invoke()` para procesar entradas y generar salidas.
- Estructura modular y escalable para facilitar futuras expansiones.

---

## 📁 Estructura del Proyecto

```bash

agentes-conversacionales-py/
├── fb/                    # Módulo para manejar la integración con Facebook Messenger
├── llm/                   # Módulo para la configuración y uso de LangChain y OpenAI
├── models/                # Definición de modelos de datos (Pydantic)
├── main.py                # Archivo principal que inicia la aplicación FastAPI
├── test_main.http         # Archivo para pruebas de endpoints HTTP
├── pyproject.toml         # Configuración del proyecto y dependencias
└── uv.lock                # Archivo de bloqueo de dependencias
```

## ⚙️ Requisitos Previos

- Python 3.13.3 o superior
- UV (https://docs.astral.sh/uv/getting-started/installation/)
- Cuenta de desarrollador en Facebook for Developers
- Clave de API de OpenAI

## 🛠️ Instalación y Configuración

1. Clonar el repositorio:

```bash

git clone https://github.com/patcornejo/agentes-conversacionales-py.git
cd agentes-conversacionales-py
```
2. Crear y activar un entorno virtual:

```bash

uv venv <<my_env>>
source <<my_env>>/bin/activate
```
3. Instalar las dependencias:
```bash

uv sync
```
4. Configurar variables de entorno:
```shell

OPENAI_API_KEY=tu_clave_de_api_de_openai
FB_VERIFY_TOKEN=tu_token_de_verificación_de_facebook
FB_PAGE_ACCESS_TOKEN=tu_token_de_acceso_de_página_de_facebook

```
5. Ejecutar la aplicación:
``` shell

uvicorn main:app --reload --port 8080
```

## 🔗 Configuración de Webhook en Facebook Messenger
1. Crear una aplicación en Facebook:
   1. Ve a Facebook for Developers y crea una nueva aplicación.
   2. Agrega el producto "Messenger" a tu aplicación.
   
2. Configurar el webhook:
   1. En la sección de configuración de Messenger, agrega la URL de tu webhook (por ejemplo, https://tu_dominio.com/webhook) y el token de verificación que definiste en el archivo .env. 
   2. Suscribe los eventos que deseas recibir, como messages y messaging_postbacks.

3. Obtener el token de acceso de la página:
   1. Genera un token de acceso para la página de Facebook que administrará el bot y agrégalo al archivo .env como FB_PAGE_ACCESS_TOKEN.

## 🧪 Pruebas

Puedes utilizar herramientas como Postman o Insomnia para probar los endpoints de la API. El archivo test_main.http proporciona ejemplos de solicitudes que puedes realizar para verificar el funcionamiento del chatbot.

## 📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT.

¡Esperamos que este proyecto te sea útil para aprender y desarrollar tus propios agentes conversacionales! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contribuir al repositorio.