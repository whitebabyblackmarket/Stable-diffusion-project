
# Stable Diffusion Image Generation Project

## Overview
This project is designed to use the Stability AI API for generating images based on text prompts. It is built using a frontend-only architecture, integrating directly with the Stability AI API without the need for a separate backend server.

## Key Features
- **Text-to-Image Generation**: Users can input text prompts to generate images.
- **Image-to-Image Modification**: The application allows for modifications of existing images based on user input.

## Technology Stack
- **Frontend**: Next.js with TypeScript
- **API**: Stability AI API for image generation

## Project Setup
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Run `npm install` to install the required dependencies.
3. **Environment Variables**: Set up the `.env.local` file with your Stability AI API key.
4. **Start the Development Server**: Run `npm run dev` to start the development server.
5. **Open the Application**: Open `http://localhost:3000` in your browser to view the application.

## Usage
- The main page provides an interface for users to input text prompts.
- After submitting a prompt, the application communicates with the Stability AI API and displays the generated image.

## Security Considerations
- API keys are secured and not exposed to the frontend.
- Direct API calls are made securely to ensure data privacy.

## Future Enhancements
- User account integration for saving generated images.
- Expanding the range of customization options for image generation.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes or enhancements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
