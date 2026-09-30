from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import asyncio

router = APIRouter()

@router.post("/chat")
async def chat(data: dict):

    message = data["message"]

    async def generate():

        # Replace this with your LLM call
        fake_response = "This is a streamed response from your AI assistant."

        for word in fake_response.split():
            yield word + " "
            await asyncio.sleep(0.1)

    return StreamingResponse(generate(), media_type="text/plain")