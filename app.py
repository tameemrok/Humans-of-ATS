from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from generate_ai import transform_image
from merge_collage import create_collage
import os

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    media_url = request.values.get('MediaUrl0', '')
    from_number = request.values.get('From', '')

    resp = MessagingResponse()

    if media_url:
        resp.message("⏳ Generating your Time Travel Face collage... Please wait!")

        eras = ["1920s", "1980s", "2020s", "2050"]
        image_urls = []

        for era in eras:
            url = transform_image(media_url, era)
            if not url:
                resp.message(f"❌ Failed to generate for {era}. Try again later.")
                return str(resp)
            image_urls.append(url)

        # Save collage
        collage_path = "static/collage.jpg"
        create_collage(image_urls, eras, collage_path)

        # Send collage
        msg = resp.message("🕰️ Here's your Time Travel Face!")
        msg.media(request.url_root + "static/collage.jpg")
    else:
        resp.message("👋 Send me a selfie and I’ll create your Time Travel collage!")

    return str(resp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
