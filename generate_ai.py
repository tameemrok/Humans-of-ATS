import replicate
import os

# Load API token from environment variable
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

# Check if token is present
if not REPLICATE_API_TOKEN:
    raise ValueError("REPLICATE_API_TOKEN is not set in environment variables.")

# Initialize client (Replicate will auto-use token from env)
replicate.Client(api_token=REPLICATE_API_TOKEN)

def transform_image(image_url: str, era_prompt: str):
    """
    Transforms the input image with a prompt based on era
    :param image_url: URL of the selfie/photo sent via WhatsApp
    :param era_prompt: e.g., "1920s", "2050s", etc.
    :return: URL of the generated AI image
    """

    # You can customize this prompt to be more detailed per era
    full_prompt = f"A {era_prompt} portrait photo of a person, cinematic lighting, highly detailed, 4K, trending on artstation"

    # SDXL full model reference with version ID
    model_ref = "stability-ai/sdxl:fc1ed08c89364a4a88e26c0b6e64798c37cfa4ce73d9e2df8169c920c936f47c"

    try:
        output = replicate.run(
            model_ref,
            input={
                "prompt": full_prompt,
                "image": image_url,
                "width": 512,
                "height": 512,
                "num_outputs": 1
            }
        )
        return output[0]  # URL of generated image
    except Exception as e:
        print(f"Error in Replicate generation: {e}")
        return None
