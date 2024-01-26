"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/2/guidelines"""
import inspect
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

def print_completion(prompt):
    """Call get_completion() & print the output"""
    print(f"""\n{inspect.stack()[1][3]}():{prompt}\n----------\n""")
    print(get_completion(prompt))
