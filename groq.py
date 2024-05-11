import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def groq_completion(user_request, page_text):
    system_prompt = """Your role is to help the reader of a book with various tasks that they want to achieve.\n
    These include:
    1. Searching the web using Brave to augment the information in the book.
    2. Storing a section of the passage that they want to remember.

    You will be provided with the text of the page they are viewing as well as their request.
    If they ask you to search, you should return json containing the key BRAVE_SEARCH and the value that is the appropriate search query.
    If they ask to store the passage, you should find out which text they want and return only the text STORE_PASSAGE.

    Here is the user request:{user_request}
    And here is the text of the page:{page_text}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": system_prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content)

    return chat_completion