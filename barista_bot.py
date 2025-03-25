import os

import vertexai
import coffee_functions

from vertexai.generative_models import FunctionDeclaration, GenerationConfig, GenerativeModel, Tool

# TODO: Rename ".env.template" to ".env" and add your project ID to it.
from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.environ.get("PROJECT_ID"), location="us-central1")

model = GenerativeModel(
    model_name="gemini-1.5-flash-002"
)
chat = model.start_chat()

print("Welcome to Barista bot!\n\n")

while True:
    response = chat.send_message(input("> "))
    print(response)
