import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



def groq_completion(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content)

    return chat_completion

