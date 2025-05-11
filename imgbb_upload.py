import requests
import os
import os

IMGBB_API_KEY = os.environ.get("IMGBB_API_KEY")
if not IMGBB_API_KEY:
    raise ValueError("❌ IMGBB_API_KEY is not set.")

def upload_to_imgbb(image_url: str) -> str:
    print(f"📤 Uploading to ImgBB: {image_url}")

    endpoint = "https://api.imgbb.com/1/upload"
    payload = {
        "key": IMGBB_API_KEY,
        "image": image_url
    }

    try:
        response = requests.post(endpoint, data=payload)
        response.raise_for_status()
        data = response.json()
        uploaded_url = data["data"]["url"]
        print(f"✅ ImgBB upload success: {uploaded_url}")
        return uploaded_url

    except Exception as e:
        print(f"❌ Failed to upload to ImgBB → {e}")
        print(f"📄 ImgBB response: {response.text}")
        return None
