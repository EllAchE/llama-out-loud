import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

system_prompt = """Your role is to help the reader of a book with various tasks that they want to achieve.\n
    These include:
    1. Searching the web using Brave to augment the information in the book.
    2. Storing a section of the passage that they want to remember.
    
    we will provide
    """

def groq_completion():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content)

    return chat_completion