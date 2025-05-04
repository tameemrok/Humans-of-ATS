import replicate
import os

# Validate token
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    raise ValueError("❌ REPLICATE_API_TOKEN is not set.")

replicate.Client(api_token=REPLICATE_API_TOKEN)

# Define prompts per era
ERA_PROMPTS = {
    "1920s": "black and white vintage 1920s portrait, studio lighting",
    "1980s": "retro 1980s pop art style selfie, vibrant colors",
    "2020s": "modern high-resolution Instagram-style selfie, realistic",
    "2050": "futuristic sci-fi cyberpunk portrait with glowing lights"
}

# Model reference (img2img)
MODEL_REF = "stability-ai/stable-diffusion-img2img:15a3689ee13b0d2616e98820eca31d4c3abcd36672df6afce5cb6feb1d66087d"

# Core transformation function
def transform_image(image_url: str, era: str):
    prompt = ERA_PROMPTS.get(era, "vintage portrait")
    
    try:
        print(f"🧠 Era: {era} | Prompt: {prompt} | Image: {image_url}")

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
            print(f"❌ No output for {era}")
            return None

        print(f"✅ Output for {era}: {output[0]}")
        return output[0]

    except Exception as e:
        print(f"❌ Replicate failed for {era} → {e}")
        return None
