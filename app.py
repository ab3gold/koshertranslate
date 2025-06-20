from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def translate_and_correct(text):
    prompt = (
        f"Correct the grammar and translate this to English:\n\n"
        f"{text}\n\n"
        f"Respond like this:\n"
        f"Corrected: ...\nTranslation: ..."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response['choices'][0]['message']['content'].strip()

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body", "").strip()
    result = translate_and_correct(incoming_msg)

    resp = MessagingResponse()
    resp.message(result)
    return str(resp)

@app.route("/")
def index():
    return "Language Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
