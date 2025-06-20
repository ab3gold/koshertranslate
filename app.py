from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body", "").strip()

    # Placeholder response for now
    response_text = f"Translation: [Placeholder for '{incoming_msg}']"

    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

@app.route("/")
def index():
    return "Language Bot is running!"

# ✅ Required for Heroku to run correctly
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
