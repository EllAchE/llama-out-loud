from openai import OpenAI
import os
import weave
from dotenv import load_dotenv
import base64
load_dotenv()


# weave.init('llama-out-loud1')

# api_key = os.getenv('OPENAI_API')
client = OpenAI()

# @weave.op()
def ocr(base64_image):
   
    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "Transcribe the text on here. Describe diagram if there are any. Be concise. If there are any blue highlighting, only return that text inside triple backslash quote with no preamble"},
            {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ],
        }
    ],
    max_tokens=300,
    )
    return response.choices[0].message.content


# test
if __name__ == "__main__":
    with open('../tester/20240511-181602.png', "rb") as file_to_encode:
        encoded_string = base64.b64encode(file_to_encode.read()).decode("utf-8")
        print(ocr(encoded_string))
