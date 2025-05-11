import requests
import os

TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")

def upload_to_replicate_delivery(image_url: str) -> str:
    print(f"📅 Downloading image from Twilio: {image_url}", flush=True)

    try:
        response = requests.get(image_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
        response.raise_for_status()
        image_binary = response.content
    except Exception as e:
        print(f"❌ Failed to download image from Twilio → {e}", flush=True)
        return None

    print("🚀 Uploading to Replicate delivery host...", flush=True)

    try:
        upload_response = requests.post(
            "https://dreambooth-api-experimental.replicate.delivery/upload",
            files={"file": ("input.jpg", image_binary, "image/jpeg")}
        )
        upload_response.raise_for_status()
        uploaded_url = upload_response.json()["url"]
        print(f"✅ Replicate-hosted image URL: {uploaded_url}", flush=True)
        return uploaded_url

    except Exception as e:
        print(f"❌ Upload to Replicate delivery failed → {e}", flush=True)
        if hasattr(e, "response"):
            print(f"📄 Error body: {e.response.text}", flush=True)
        return None
