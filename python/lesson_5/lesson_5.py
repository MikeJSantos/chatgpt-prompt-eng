"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/5/inferring"""
from openai_wrapper import print_completion

LAMP_REVIEW = """
Needed a nice lamp for my bedroom, and this one had additional storage and not too high of a price point. Got it fast.
The string to our lamp broke during the transit and the company happily sent over a new one. Came within a few days as well.
It was easy to put together.  I had a missing part, so I contacted their support and they very quickly got me the missing piece!
Lumina seems to me to be a great company that cares about their customers and products!!
"""

def sentiment():
    """Basic Sentiment"""
    prompt = f"""
        What is the sentiment of the following product review, 
        which is delimited with triple backticks?

        Review text:
        '''
        {LAMP_REVIEW}
        '''
    """
    print_completion(prompt)

sentiment()
