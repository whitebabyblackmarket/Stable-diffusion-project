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
        logging.error("API key not configured")
        raise HTTPException(status_code=500, detail="API key not configured")

    # Replace {engine_id} with the appropriate engine ID from Stability AI
    url = "https://api.stability.ai/v1/generation/{engine_id}/text-to-image"  
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "text_prompts": [{"text": prompt, "weight": 1.0}],
        "cfg_scale": 7,
        "height": 512,
        "width": 512,
        "style_preset": "photographic",  # Can be changed as needed
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        logging.error(f"Error in text-to-image generation: {response.content}")
        raise HTTPException(status_code=response.status_code, detail=str(response.content))

    logging.info("Text-to-image generation successful")
    return Response(content=response.content, media_type="image/png")

@router.post("/generate-image-to-image")
def generate_image_to_image(image: UploadFile = File(...), prompt: str = Form(...)):
    api_key = get_api_key()
    if not api_key:
        logging.error("API key not configured")
        raise HTTPException(status_code=500, detail="API key not configured")

    # Replace {engine_id} with the appropriate engine ID
    url = "https://api.stability.ai/v1/generation/{engine_id}/image-to-image"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    files = {
        "init_image": (image.filename, image.file, "image/png"),
        "text_prompts": (None, f"[{{\"text\": \"{prompt}\", \"weight\": 1.0}}]", "application/json"),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        logging.error(f"Error in image-to-image generation: {response.content}")
        raise HTTPException(status_code=response.status_code, detail=str(response.content))

    logging.info("Image-to-image generation successful")
    return Response(content=response.content, media_type="image/png")


