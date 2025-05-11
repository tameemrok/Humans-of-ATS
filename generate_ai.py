import replicate
import os

# Load API token
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    raise ValueError("❌ REPLICATE_API_TOKEN is not set.", flush=True)

# Replicate client auto-picks from env
replicate.Client(api_token=REPLICATE_API_TOKEN)

# Style prompts by era
ERA_PROMPTS = {
    "1920s": "a black and white vintage portrait, 1920s, realistic, studio lighting",
    "1980s": "a retro pop art selfie, 1980s style, colorful, close-up",
    "2020s": "modern Instagram selfie, clean skin, shallow depth of field",
    "2050": "futuristic sci-fi cyberpunk portrait, glowing effects, fantasy lighting"
}

# Replicate model: stable-diffusion-img2img
MODEL_REF = "stability-ai/stable-diffusion-img2img:15a3689ee13b0d2616e98820eca31d4c3abcd36672df6afce5cb6feb1d66087d"

def transform_image(image_url: str, era: str):
    prompt = ERA_PROMPTS.get(era, "vintage portrait")
    print(f"🧠 Sending to Replicate → Prompt: '{prompt}', Image URL: {image_url}", flush=True)

    try:
        output = replicate.run(
            MODEL_REF,
            input={
                "image": image_url,
                "prompt": prompt,
                "scheduler": "DPMSolverMultistep",
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "prompt_strength": 0.8,
                "num_inference_steps": 25
            }
        )

        if not output or not output[0]:
            print(f"❌ No output from Replicate for era {era}. Raw output: {output}", flush=True)
            return None

        print(f"✅ Replicate image for {era}: {output[0]}", flush=True)
        return output[0]

    except Exception as e:
        print(f"❌ Error from Replicate for {era}: {e}", flush=True)
        return None
