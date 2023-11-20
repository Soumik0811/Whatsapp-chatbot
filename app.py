from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from twilio.rest import Client

account_sid = 'AC0996917758ba4416b7826310a0cd90a3'
auth_token = 'ded8c4f728b50bc90adffcdc32c4b8c0'

app = Flask(__name__)
api_key = os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=api_key)

def generate_answer(question):
    result = chat(
        [
            SystemMessage(content='You are the strongest person on earth and you have too much pride, but you give medium answers with 100 words adn gives some links whenever neccessary'),
            HumanMessage(content=question)
        ]
    )
    res = result.content
    return res

@app.route("/whatsapp", methods=['POST'])
def wa_reply():
    query = request.form.get('Body').lower()
    print("User Query: ", query)

    answer = generate_answer(query)

    # Send the answer back to the user's WhatsApp number using the Twilio API
    client = Client(account_sid, auth_token)
    client.messages.create(
        from_='whatsapp:+14155238886',
        to='whatsapp:+918240161499',
        body=answer
    )

    return str(answer)