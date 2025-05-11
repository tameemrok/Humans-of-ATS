import requests
import os

IMGBB_API_KEY = os.environ.get("IMGBB_API_KEY")
if not IMGBB_API_KEY:
    raise ValueError("❌ IMGBB_API_KEY is not set.", flush=True)

def upload_to_imgbb(image_url: str) -> str:
    print(f"📤 Uploading to ImgBB: {image_url}", flush=True)

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
        print(f"✅ ImgBB upload success: {uploaded_url}", flush=True)
        return uploaded_url

    except Exception as e:
        print(f"❌ ImgBB Exception: {e}", flush=True)
        if hasattr(e, "response"):
            print(f"📄 ImgBB Error response: {e.response.text}", flush=True)
        return None
