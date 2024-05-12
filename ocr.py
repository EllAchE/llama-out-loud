from openai import OpenAI
import os


def ocr(url):
    api_key = os.getenv('OPENAI_API')
    client = OpenAI(api_key=api_key)
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
    return response.choices[0].message.content

if __name__ == "__main__":
    print(ocr(url = "https://github.com/EllAchE/llama-out-loud/blob/ocr/image/zoom_book.png?raw=true"))
