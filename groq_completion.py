import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def groq_completion(prompt):
    print("prompt", prompt)
    completion_objct = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        # model="llama3-8b-8192",
        model="llama3-70b-8192",
    )

    return completion_objct.choices[0].message.content
