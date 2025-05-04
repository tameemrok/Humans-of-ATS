import replicate
import os

# Get your Replicate API token from environment variables
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    raise ValueError("❌ REPLICATE_API_TOKEN is not set in environment variables.")

# Replicate client auto-picks up from env
replicate.Client(api_token=REPLICATE_API_TOKEN)

# Valid styles supported by the model
ERA_STYLES = {
    "1920s": "vintage",     # Classic black & white vibe
    "1980s": "pop-art",     # Bold, colorful retro style
    "2020s": "cyberpunk",   # Modern tech aesthetic
    "2050": "fantasy"       # Imaginative futuristic concept
}

# Optional fallback if Replicate fails
DEFAULT_STYLE = "vintage"

def transform_image(image_url: str, era: str):
    style = ERA_STYLES.get(era, "vintage")

    # Replace with a known good image (for testing only)
    image_url = "https://replicate.delivery/pbxt/XhzKvzzsNcUxb0BQn1kOzJ1aD5EoU2Thg1cqSWYc0V1KLODZ/output.png"

    model_ref = "cjwbw/style-transfer:7ce1044b8fa726adb5fd23cb47a9a421664eb05c23f2e1f64b82d47a52c74a30"

    output = replicate.run(
        model_ref,
        input={"image": image_url, "style": style}
    )

    return output[0] if output and output[0] else None


    except Exception as e:
        print(f"❌ Error generating image for {era} → {e}")
        return None
