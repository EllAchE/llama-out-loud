def download_pdf(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download PDF: Status code {response.status_code}")


def convert_pdf_to_images(pdf_data):
    # convert from bytes is a library function that returns an array
    images = convert_from_bytes(pdf_data)
    return images.pop()


# TODO: We could resize the images here so that the cost is lower (they might be resized to squares?)
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


pdf_url = "https://www.nj.gov/oag/ge/docs/Financials/IGRTaxReturns/2016/January2016.pdf"

# Download PDF
pdf_data = download_pdf(pdf_url)

# Convert PDF to images
image = convert_pdf_to_images(pdf_data)

# save image locally
image_path = "image.png"
image.save(image_path)

base64_image = encode_image(image_path)
print("Image encoded")

# Save the encoding to a .txt file
with open("image.txt", "w") as f:
    f.write(base64_image)

import openai

response = openai.ChatCompletion.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": ""
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
    max_tokens=300,
)

print("Sending request to OpenAI")

response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
)

print(response.status_code)

print(response.json())
