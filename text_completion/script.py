import os
from openai import OpenAI
client = OpenAI()
messages = [
    {
        "role": "user",
        "content": "Sarah has 5 brothers. Each of Sarah's brothers has 2 sisters. How many sisters does Sarah have in total?",
    }
]
print(f"Prompt:\n{messages[0]['content']}\n")
models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-0125-preview"]
for model in models:
    print(f"\n---\nGenerating chat completion with {model}:\n")
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
        