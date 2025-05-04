import replicate
import os

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    raise ValueError("❌ REPLICATE_API_TOKEN is not set.")

replicate.Client(api_token=REPLICATE_API_TOKEN)

ERA_STYLES = {
    "1920s": "vintage",
    "1980s": "pop-art",
    "2020s": "cyberpunk",
    "2050": "fantasy"
}

DEFAULT_STYLE = "vintage"

def transform_image(image_url: str, era: str):
    style = ERA_STYLES.get(era, DEFAULT_STYLE)

    # 🚨 Force known-good image for now
    image_url = "https://replicate.delivery/pbxt/XhzKvzzsNcUxb0BQn1kOzJ1aD5EoU2Thg1cqSWYc0V1KLODZ/output.png"

    model_ref = "cjwbw/style-transfer:7ce1044b8fa726adb5fd23cb47a9a421664eb05c23f2e1f64b82d47a52c74a30"

    try:
        print(f"🧠 Generating '{style}' style for era '{era}'...")

        output = replicate.run(
            model_ref,
            input={"image": image_url, "style": style}
        )

        if not output or not output[0]:
            print("❌ Replicate returned no image.")
            return None

        print("✅ Replicate image URL:", output[0])
        return output[0]

    except Exception as e:
        print(f"❌ Error in transform_image(): {e}")
        return None
