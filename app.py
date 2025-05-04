from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '')
    from_number = request.values.get('From', '')
    media_url = request.values.get('MediaUrl0', '')

    print(f"Message from {from_number}: {incoming_msg}")
    print(f"Media URL: {media_url}")

    resp = MessagingResponse()
    msg = resp.message("Thanks! You will receive your Time Travel Face collage shortly.")
    return str(resp)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
