from fastapi import FastAPI
from .routers import image_generation

app = FastAPI()

# Include the router from image_generation.py in the FastAPI app
# This makes the endpoints defined in image_generation accessible
app.include_router(image_generation.router)

