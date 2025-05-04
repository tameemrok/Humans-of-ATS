import replicate
import os

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    raise ValueError("REPLICATE_API_TOKEN is not set in environment variables.")

# Replicate client will auto-pick from env
replicate.Client(api_token=REPLICATE_API_TOKEN)

# Mapping eras to visual styles
ERA_STYLES = {
    "1920s": "vintage",
    "1980s": "cubism",
    "2020s": "pop-art",
    "2050": "cyberpunk"
}

def transform_image(image_url: str, era: str):
    style = ERA_STYLES.get(era, "vintage")

    model_ref = "cjwbw/style-transfer:7ce1044b8fa726adb5fd23cb47a9a421664eb05c23f2e1f64b82d47a52c74a30"

    try:
        output = replicate.run(
            model_ref,
            input={
                "image": image_url,
                "style": style
            }
        )

        if not output or not output[0]:
            print(f"❌ No output from Replicate for era: {era}")
            return None

        return output[0]  # URL of generated image

    except Exception as e:
        print(f"❌ Error in transform_image(): {e}")
        return None
