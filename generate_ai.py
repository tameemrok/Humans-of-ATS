import replicate
import os

# This function takes an image URL and an era prompt (like "1920s") and returns a generated image URL
def transform_image(image_url: str, era_prompt: str):
    replicate_api_token = os.environ.get("REPLICATE_API_TOKEN")
    if not replicate_api_token:
        raise Exception("Replicate API token not found")

    replicate.Client(api_token=replicate_api_token)

    full_prompt = f"A {era_prompt} photo of a person, cinematic lighting, high detail portrait"

    output = replicate.run(
        "stability-ai/sdxl",
        input={
            "prompt": full_prompt,
            "image": image_url,
            "width": 512,
            "height": 512,
            "num_outputs": 1
        }
    )

    return output[0]
