from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.get("/")
def home():
    return "ok", 200

@app.get("/voice")
def voice_check():
    return "voice endpoint alive", 200

@app.route("/voice", methods=["POST"])
def handle_call():
    response = VoiceResponse()
    response.say("Hey! This is your AI assistant. Leave a message and I’ll send it to the business owner.")
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
