from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Check for required environment variables
api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv('OPENAI_BASE_URL')

if not api_key or not base_url:
    print("Error: Missing required environment variables.")
    print("Please ensure OPENAI_API_KEY and OPENAI_BASE_URL are set in your .env file.")
    sys.exit(1)

client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)

completion = client.chat.completions.create(
  extra_body={},
  model="openai/gpt-4o-2024-11-20",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
          }
        }
      ]
    }
  ]
)

print(completion.choices[0].message.content)
