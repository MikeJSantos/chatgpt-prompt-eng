"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/5/inferring"""
from openai_wrapper import print_completion

LAMP_REVIEW = """
Review text:
'''
Needed a nice lamp for my bedroom, and this one had additional storage and not too high of a price point. Got it fast.
The string to our lamp broke during the transit and the company happily sent over a new one. Came within a few days as well.
It was easy to put together.  I had a missing part, so I contacted their support and they very quickly got me the missing piece!
Lumina seems to me to be a great company that cares about their customers and products!!
```
"""

def sentiment():
    """Basic Sentiment"""
    prompt = f"""
        What is the sentiment of the following product review, 
        which is delimited with triple backticks?

        {LAMP_REVIEW}
    """
    print_completion(prompt)

def sentiment_one_word():
    """Sentiment: one word answer"""
    prompt = f"""
        What is the sentiment of the following product review, which is delimited with triple backticks?

        Give your answer as a single word, either "positive" or "negative".

        {LAMP_REVIEW}
    """
    print_completion(prompt)

def identify_emotions():
    """Identify types of emotions"""
    prompt = f"""
        Identify a list of emotions that the writer of the following review is expressing.
        Include no more than five items in the list.
        Format your answer as a list of lower-case words separated by commas.

        {LAMP_REVIEW}
    """
    print_completion(prompt)

def identify_item_and_company():
    """Extract product and company name from customer reviews"""
    prompt = f"""
        Identify the following items from the review text: 
        - Item purchased by reviewer
        - Company that made the item

        The review is delimited with triple backticks.
        Format your response as a JSON object with "Item" and "Brand" as the keys. 
        If the information isn't present, use "unknown" as the value.
        Make your response as short as possible.

        {LAMP_REVIEW}
    """
    print_completion(prompt)

# sentiment()
# sentiment_one_word()
# identify_emotions()
identify_item_and_company()
