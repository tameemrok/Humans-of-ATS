import cloudinary
import cloudinary.uploader
import requests
import os

TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

def upload_to_cloudinary(image_url: str) -> str:
    try:
        print(f"📅 Downloading image from Twilio: {image_url}", flush=True)
        response = requests.get(image_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
        response.raise_for_status()
        image_data = response.content

        print("🚀 Uploading to Cloudinary...", flush=True)
        upload_result = cloudinary.uploader.upload(image_data, resource_type="image")

        url = upload_result.get("secure_url")
        print(f"✅ Cloudinary image URL: {url}", flush=True)
        return url
    except Exception as e:
        print(f"❌ Cloudinary upload failed: {e}", flush=True)
        return None
