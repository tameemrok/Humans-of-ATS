import replicate
import os

# Get your Replicate API token from environment variables
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    raise ValueError("❌ REPLICATE_API_TOKEN is not set in environment variables.")

# Initialize Replicate client
replicate.Client(api_token=REPLICATE_API_TOKEN)

# Valid styles supported by the style-transfer model
ERA_STYLES = {
    "1920s": "vintage",
    "1980s": "pop-art",
    "2020s": "cyberpunk",
    "2050": "fantasy"
}

DEFAULT_STYLE = "vintage"

def transform_image(image_url: str, era: str):
    # Map era to supported style
    style = ERA_STYLES.get(era, DEFAULT_STYLE)

    # 🧪 TEST ONLY: Override with a known working image to isolate failures
    image_url = "https://replicate.delivery/pbxt/XhzKvzzsNcUxb0BQn1kOzJ1aD5EoU2Thg1cqSWYc0V1KLODZ/output.png"

    # Use Replicate's style-transfer model that supports image input
    model_ref = "cjwbw/style-transfer:7ce1044b8fa726adb5fd23cb47a9a421664eb05c23f2e1f64b82d47a52c74a30"

    try:
        print(f"🎨 Generating style '{style}' for era '{era}'...")

        output = replicate.run(
            model_ref,
            input={
                "image": image_url,
                "style": style
            }
        )

        if not output or not output[0]:
            print(f"❌ No output returned from Replicate for era: {era}")
            return None

        print(f"✅ Image generated for {era}: {output[0]}")
        return output[0]

    except Exception as e:
        print(f"❌ Error generating image for {era}: {e}")
        return None
