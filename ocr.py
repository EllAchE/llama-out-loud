from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_API')
client = OpenAI(api_key=api_key)

url = "https://github.com/EllAchE/llama-out-loud/blob/ocr/image/book.jpeg?raw=true"

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Transcribe what the book says"},
        {
          "type": "image_url",
          "image_url": {
            "url": url,
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])