from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    response.say("Hello! Please leave a message after the beep.")
    response.record(maxLength="30", action="/complete")
    return Response(str(response), mimetype="text/xml")

@app.route("/complete", methods=["POST"])
def complete():
    return "Voicemail received", 200

@app.route("/", methods=["GET"])
def index():
    return "App is running", 200
