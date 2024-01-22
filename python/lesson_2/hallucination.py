"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/2/guidelines"""
from openai_wrapper import print_completion

def hallucination():
    """Boie is a real company, the product name is not real."""
    prompt = """
        Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
    """
    print_completion(prompt)

hallucination()
