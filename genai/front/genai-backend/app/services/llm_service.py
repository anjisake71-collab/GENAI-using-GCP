import os
import certifi

# Fix SSL for corporate proxy
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = certifi.where()
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

import vertexai
from vertexai.generative_models import GenerativeModel
from app.config import PROJECT_ID, LOCATION, MODEL_NAME
import asyncio

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel(MODEL_NAME)


# NORMAL RESPONSE (non-streaming)
def generate_response(prompt: str) -> str:

    response = model.generate_content(prompt)

    return response.text


# STREAMING RESPONSE
async def stream_response(prompt: str):

    response = model.generate_content(prompt)

    text = response.text

    words = text.split()

    for word in words:
        yield word + " "
        await asyncio.sleep(0.03)
