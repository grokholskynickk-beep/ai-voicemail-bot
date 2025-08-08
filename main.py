from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# Simple health checks so a browser GET works
@app.get("/")
def root():
    return "ok", 200

@app.get("/health")
def health():
    return "healthy", 200

# Allow GET for quick browser testing, keep POST for Twilio
@app.route("/voice", methods=["GET", "POST"])
def voice():
    if request.method == "GET":
        return "voice endpoint up", 200

    resp = VoiceResponse()
    resp.say("Hey! This is your AI assistant. Leave a message and I’ll send it to the business owner.")
    return str(resp)

if __name__ == "__main__":
    # run on 0.0.0.0:8080 for Fly
    app.run(host="0.0.0.0", port=8080)
