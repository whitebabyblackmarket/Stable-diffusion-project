# dependencies.py
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
# This is where the Stability API key is stored
load_dotenv()

def get_api_key():
    # Retrieve the Stability API key from environment variables
    return os.getenv("STABILITY_API_KEY")


