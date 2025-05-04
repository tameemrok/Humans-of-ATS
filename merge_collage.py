from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def create_collage(image_urls, labels, output_path="collage.jpg"):
    assert len(image_urls) == 4 and len(labels) == 4

    images = [Image.open(BytesIO(requests.get(url).content)).resize((512, 512)) for url in image_urls]
    collage = Image.new("RGB", (1024, 1024))

    # Load default font
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()

    draw_positions = [(0, 0), (512, 0), (0, 512), (512, 512)]

    for i, img in enumerate(images):
        collage.paste(img, draw_positions[i])
        draw = ImageDraw.Draw(collage)
        draw.text((draw_positions[i][0]+10, draw_positions[i][1]+10), labels[i], fill="white", font=font)

    collage.save(output_path)
    return output_path
