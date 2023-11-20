from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from twilio.rest import Client

account_sid = #your account sid from twilio
auth_token = #your auth token from twilio

app = Flask(__name__)
api_key = os.getenv('OPENAI_API_KEY') #your open ai api key
chat = ChatOpenAI(openai_api_key=api_key)

def generate_answer(question):
    result = chat(
        [
            SystemMessage(content='You are the strongest person on earth and you have too much pride, but you give medium answers with 100 words adn gives some links whenever neccessary'), #You can decide on the character of your bot.
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
        to='whatsapp: #give you number here',
        body=answer
    )

    return str(answer)
