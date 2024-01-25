"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/4/summarizing"""
from openai_wrapper import print_completion

PRODUCT_REVIEW = """Review:
```
Got this panda plush toy for my daughter's birthday, who loves it and takes it everywhere.
It's soft and super cute, and its face has a friendly look.
It's a bit small for what I paid though.
I think there might be other options that are bigger for the same price.
It arrived a day earlier than expected, so I got to play with it myself before I gave it to her.
```
"""

def summarize_word_sentence_character_limit():
    """Summarize with a word/sentence/character limit"""
    prompt = f"""
        Your task is to generate a short summary of a product review from an ecommerce site. 
        Summarize the review below, delimited by triple backticks, in at most 30 words. 

        {PRODUCT_REVIEW}
    """
    print_completion(prompt)

def summarize_shipping_and_delivery():
    """Summarize with a focus on shipping and delivery"""
    prompt = f"""
        Your task is to generate a short summary of a product review from an ecommerce site to give feedback to the Shipping deparmtment. 
        Summarize the review below, delimited by triple backticks, in at most 30 words, and focusing on any aspects that mention shipping and delivery of the product. 

        {PRODUCT_REVIEW}
    """
    print_completion(prompt)

def summarize_price_and_value():
    """Summarize with a focus on price and value"""
    prompt = f"""
        Your task is to generate a short summary of a product review from an ecommerce site to give feedback to the pricing deparmtment,
        responsible for determining the price of the product.  

        Summarize the review below, delimited by triple backticks, in at most 30 words, 
        and focusing on any aspects that are relevant to the price and perceived value. 

        {PRODUCT_REVIEW}
    """
    print_completion(prompt)

def extract():
    """Try "extract" instead of "summarize"""
    prompt = f"""
        Your task is to extract relevant information from a product review from an ecommerce site to give feedback to the Shipping department. 
        From the review below, delimited by triple quotes extract the information relevant to shipping and delivery. Limit to 30 words.
        
        {PRODUCT_REVIEW}
    """
    print_completion(prompt)

summarize_word_sentence_character_limit()
summarize_shipping_and_delivery()
summarize_price_and_value()
extract()
