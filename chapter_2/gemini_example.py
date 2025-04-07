import os
from dotenv import load_dotenv
from google import genai

# pip install genai google-api-python-client google-genai
# install rust
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please check your .env file.")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)