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
    # Map era to style
    style = ERA_STYLES.get(era, DEFAULT_STYLE)

    model_ref = "cjwbw/style-transfer:7ce1044b8fa726adb5fd23cb47a9a421664eb05c23f2e1f64b82d47a52c74a30"

    try:
        print(f"🧠 Requesting style: '{style}' for era: '{era}'")

        output = replicate.run(
            model_ref,
            input={
                "image": image_url,
                "style": style
            }
        )

        if not output or not output[0]:
            print(f"❌ No output from Replicate for era: {era}, style: {style}")
            return None

        print(f"✅ Image generated for {era}: {output[0]}")
        return output[0]  # URL of generated image

    except Exception as e:
        print(f"❌ Error generating image for {era} → {e}")
        return None
