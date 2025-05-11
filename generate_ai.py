import os
import requests

HUGGINGFACE_TOKEN = os.environ.get("HUGGINGFACE_TOKEN")
if not HUGGINGFACE_TOKEN:
    raise ValueError("HUGGINGFACE_TOKEN is not set", flush=True)

API_URL = "https://api-inference.huggingface.co/models/InstantX/InstantID"
headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

ERA_PROMPTS = {
    "1920s": "portrait in 1920s vintage style, black and white, dramatic lighting",
    "1980s": "retro 1980s headshot, neon tones, pop art styling",
    "2020s": "modern instagram selfie, realistic lighting, minimal edit",
    "2050": "futuristic sci-fi look, glowing cyberpunk background"
}

def transform_image(image_url: str, era: str):
    prompt = ERA_PROMPTS.get(era, "vintage style photo")
    print(f"🧠 Sending to HuggingFace → Prompt: '{prompt}', Image URL: {image_url}", flush=True)

    try:
        payload = {
            "inputs": {
                "image": image_url,
                "prompt": prompt
            }
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        output = response.json()

        if isinstance(output, list) and output and 'url' in output[0]:
            print(f"✅ HuggingFace output URL: {output[0]['url']}", flush=True)
            return output[0]['url']

        print(f"❌ Unexpected HuggingFace output: {output}", flush=True)
        return None

    except Exception as e:
        print(f"❌ Error from HuggingFace for {era}: {e}", flush=True)
        return None
