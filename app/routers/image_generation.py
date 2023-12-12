from fastapi import APIRouter, HTTPException, Form, UploadFile, File, Response
import requests
from ..dependencies import get_api_key
import logging

# Setting up basic logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()

@router.post("/generate-text-to-image")
def generate_text_to_image(prompt: str = Form(...)):
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
    data = {
        "text_prompts": [{"text": prompt, "weight": 1.0}],
        "cfg_scale": 7,
        "height": 512,
        "width": 512,
        "style_preset": "photographic",  # Default style preset
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        error_message = f"Error in text-to-image generation: Status Code: {response.status_code}, Response: {response.content}"
        logging.error(error_message)
        raise HTTPException(status_code=response.status_code, detail=error_message)

    logging.info("Text-to-image generation successful")
    return Response(content=response.content, media_type="image/png")

@router.post("/generate-image-to-image")
def generate_image_to_image(image: UploadFile = File(...), prompt: str = Form(...)):
    api_key = get_api_key()
    if not api_key:
        error_message = "API key not configured. Please check the .env file or dependencies.py."
        logging.error(error_message)
        raise HTTPException(status_code=500, detail=error_message)

    engine_id = "stable-diffusion-v1-6"  # Engine ID for Stable Diffusion v1.6
    url = f"https://api.stability.ai/v1/generation/{engine_id}/image-to-image"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    files = {
        "init_image": (image.filename, image.file, "image/png"),
        "text_prompts": (None, f"[{{\"text\": \"{prompt}\", \"weight\": 1.0}}]", "application/json"),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        error_message = f"Error in image-to-image generation: Status Code: {response.status_code}, Response: {response.content}"
        logging.error(error_message)
        raise HTTPException(status_code=response.status_code, detail=error_message)

    logging.info("Image-to-image generation successful")
    return Response(content=response.content, media_type="image/png")



