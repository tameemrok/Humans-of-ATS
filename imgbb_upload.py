import requests
import os
from base64 import b64encode

IMGBB_API_KEY = os.environ.get("IMGBB_API_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")

if not IMGBB_API_KEY:
    raise ValueError("❌ IMGBB_API_KEY is not set.", flush=True)

def upload_to_imgbb(image_url: str) -> str:
    print(f"📤 Downloading image from Twilio: {image_url}", flush=True)

    try:
        # Download image from Twilio
        response = requests.get(image_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
        response.raise_for_status()
        image_binary = response.content
        image_base64 = b64encode(image_binary).decode("utf-8")
    except Exception as e:
        print(f"❌ Failed to download image from Twilio → {e}", flush=True)
        return None

    print("📤 Uploading to ImgBB...", flush=True)

    try:
        res = requests.post(
            "https://api.imgbb.com/1/upload",
            data={
                "key": IMGBB_API_KEY,
                "image": image_base64
            }
        )
        res.raise_for_status()
        url = res.json()["data"]["url"]
        print(f"✅ ImgBB upload success: {url}", flush=True)
        return url

    except Exception as e:
        print(f"❌ ImgBB Exception: {e}", flush=True)
        if hasattr(e, "response"):
            print(f"📄 ImgBB Error response: {e.response.text}", flush=True)
        return None
