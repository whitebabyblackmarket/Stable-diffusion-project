from fastapi import APIRouter, HTTPException, Request, Response
import requests
from ..dependencies import get_api_key
import logging
from pydantic import BaseModel

# Setting up basic logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()

class TextToImageRequest(BaseModel):
    steps: int
    width: int
    height: int
    seed: int
    cfg_scale: float
    samples: int
    text_prompts: list

@router.post("/generate-text-to-image")
async def generate_text_to_image(request: TextToImageRequest):
    api_key = get_api_key()
    if not api_key:
        error_message = "API key not configured. Please check the .env file or dependencies.py."
        logging.error(error_message)
        raise HTTPException(status_code=500, detail=error_message)

    engine_id = "stable-diffusion-v1-6"  # Engine ID for Stable Diffusion v1.6
    url = f"https://api.stability.ai/v1/generation/{engine_id}/text-to-image"  
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Sending the request to Stability AI API
    response = requests.post(url, headers=headers, json=request.dict())

    if response.status_code != 200:
        error_message = f"Error in text-to-image generation: Status Code: {response.status_code}, Response: {response.content}"
        logging.error(error_message)
        raise HTTPException(status_code=response.status_code, detail=error_message)

    logging.info("Text-to-image generation successful")
    return Response(content=response.content, media_type="image/png")




