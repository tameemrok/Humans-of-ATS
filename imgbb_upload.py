import requests
import os

IMGBB_API_KEY = os.environ.get("IMGBB_API_KEY")
if not IMGBB_API_KEY:
    raise ValueError("❌ IMGBB_API_KEY is not set.")

def upload_to_imgbb(image_url: str) -> str:
    endpoint = "https://api.imgbb.com/1/upload"
    payload = {
        "key": IMGBB_API_KEY,
        "image": image_url
    }

    try:
        response = requests.post(endpoint, data=payload)
        response.raise_for_status()
        data = response.json()
        return data["data"]["url"]
    except Exception as e:
        print(f"❌ Failed to upload to ImgBB: {e}")
        return None
