from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from generate_ai import transform_image
from cloudinary_upload import upload_to_cloudinary
from merge_collage import create_collage
import os


app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    print("⚙️ WhatsApp webhook triggered", flush=True)
    incoming_msg = request.values.get("Body", "").lower()
    media_url = request.values.get("MediaUrl0", "")
    from_number = request.values.get("From", "")

    print(f"📸 Incoming WhatsApp Media URL: {media_url}", flush=True)

    resp = MessagingResponse()

    if media_url:
        resp.message("⏳ Processing your image... Please wait...")

        selfie_url = upload_to_cloudinary(media_url)
        if not selfie_url:
            print("❌ Image upload failed, aborting.", flush=True)
            resp.message("❌ Failed to process image. Try again.")
            return str(resp)

        print(f"🌐 Image available at: {selfie_url}", flush=True)

        eras = ["1920s", "1980s", "2020s", "2050"]
        image_urls = []

        for era in eras:
            print(f"🧪 Generating for: {era}", flush=True)
            url = transform_image(selfie_url, era)
            if not url:
                print(f"❌ Generation failed for {era}", flush=True)
                resp.message(f"❌ Failed to generate for {era}. Try again later.")
                return str(resp)
            image_urls.append(url)

        collage_path = "static/collage.jpg"
        create_collage(image_urls, eras, collage_path)

        msg = resp.message("🕰️ Here's your Time Travel Face!")
        msg.media(request.url_root + "static/collage.jpg")
    else:
        print("❌ No image received in WhatsApp message", flush=True)
        resp.message("👋 Please send a selfie to get started!")

    print("✅ WhatsApp request completed" flush=True)
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
