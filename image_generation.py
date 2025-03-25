import os
import PIL
import vertexai
from vertexai.vision_models import Image, ImageGenerationModel

# TODO: Rename ".env.template" to ".env" and add your project ID to it.
from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.environ.get("PROJECT_ID"), location="us-central1")

generation_model = ImageGenerationModel.from_pretrained("imagegeneration@006")

image_prompt = "a corgi sitting on a park bench"

response = generation_model.generate_images(
   prompt=image_prompt
)

response.images[0].save("corgi.png")
