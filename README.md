# WhatsApp Chatbot using Python, Flask, and OpenAI

## Project Overview
This project aims to create a conversational chatbot on WhatsApp using Python, Flask, OpenAI, Twilio API, and Ngrok. It leverages Flask to handle Twilio requests, integrates with OpenAI for generating responses, and uses Ngrok to expose the local Flask server.

### Files Included
- `app.py`: Flask application handling Twilio requests and integrating with OpenAI.
- `ngrok.exe`: Ngrok executable for exposing the local Flask server.

### Setup Instructions
#### Prerequisites
- Python 3.x installed
- Ngrok installed and set up
- Twilio account with WhatsApp Sandbox configured
- OpenAI API key

#### Installation Steps
1. Clone or download the repository:
    ```bash
    git clone https://github.com/your-username/whatsapp-chatbot.git
    cd whatsapp-chatbot
    ```
2. Set up configuration:
    - Rename `.env.example` file to `.env` and fill in necessary environment variables:
        - `TWILIO_ACCOUNT_SID`: Your Twilio account SID
        - `TWILIO_AUTH_TOKEN`: Your Twilio authentication token
        - `TWILIO_PHONE_NUMBER`: Your Twilio phone number
        - `OPENAI_API_KEY`: Your OpenAI API key

3. Run Ngrok to expose your local Flask server:
    ```bash
    ngrok http 5000
    ```
    Copy the Ngrok URL (e.g., `https://randomstring.ngrok.io`) and use it in the Twilio WhatsApp Sandbox configuration.

5. Run the Flask application:
    ```bash
    python -m flask run
    ```

#### Usage
- Access the Twilio WhatsApp Sandbox using your configured Twilio phone number.
- Interact with the chatbot via WhatsApp. The chatbot will use OpenAI for generating responses based on user queries or messages.
