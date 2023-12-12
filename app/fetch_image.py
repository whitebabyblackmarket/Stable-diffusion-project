import requests
import os
import base64
from datetime import datetime

# Create a directory for saved images if it doesn't exist
image_dir = 'saved_images'
os.makedirs(image_dir, exist_ok=True)

# Endpoint URL
url = 'http://127.0.0.1:8000/generate-text-to-image'

# Headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'  # Expecting a JSON response
}

# Data to be sent to the API Put your prompt in here for now
data = {
    'prompt': 'a race car'  # Replace with your desired prompt
}

# Sending a POST request to the FastAPI server
response = requests.post(url, headers=headers, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    
    # Extract the base64 encoded image
    base64_image = response_json['artifacts'][0]['base64']

    # Decode the base64 string into binary data
    image_data = base64.b64decode(base64_image)

    # Generate a unique filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'generated_image_{timestamp}.png'
    filepath = os.path.join(image_dir, filename)

    # Save the image
    with open(filepath, 'wb') as file:
        file.write(image_data)
    print(f"Image saved as '{filepath}'")
else:
    print(f"Error: {response.status_code}, {response.text}")



