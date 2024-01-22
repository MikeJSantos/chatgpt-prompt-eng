"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/2/guidelines"""
from os import environ
from openai import OpenAI

def get_completion(prompt, model="gpt-3.5-turbo"):
    """returns chat completion content"""
    client = OpenAI(
        api_key=environ.get("OPENAI_API_KEY")
    )
    messages = [{"role": "user", "content": prompt}]
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return chat_completion.choices[0].message.content