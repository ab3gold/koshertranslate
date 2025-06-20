from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body", "").strip()

    # For now, just return a placeholder translation
    response_text = f"Translation: [Placeholder for '{incoming_msg}']"

    # Build the Twilio response
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

@app.route("/")
def index():
    return "Language Bot is running!"
