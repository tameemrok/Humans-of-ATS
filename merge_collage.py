from PIL import Image
from io import BytesIO
import requests

def create_collage(image_urls, labels, output_path="static/collage.jpg"):
    print(f"🗁 Creating collage from {len(image_urls)} images...", flush=True)

    images = [Image.open(BytesIO(requests.get(url).content)).resize((512, 512)) for url in image_urls]
    collage = Image.new("RGB", (len(images) * 512, 512))

    for i, img in enumerate(images):
        collage.paste(img, (i * 512, 0))

    collage.save(output_path)
    print(f"✅ Collage saved at {output_path}", flush=True)
