"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/5/inferring"""
from openai_wrapper import print_completion, get_completion

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

def identify_multiple_items():
    """Doing multiple tasks at once"""
    prompt = f"""
        Identify the following items from the review text: 
        - Sentiment (positive or negative)
        - Is the reviewer expressing anger? (true or false)
        - Item purchased by reviewer
        - Company that made the item

        The review is delimited with triple backticks. \
        Format your response as a JSON object with \
        "Sentiment", "Anger", "Item" and "Brand" as the keys.
        If the information isn't present, use "unknown" \
        as the value.
        Make your response as short as possible.
        Format the Anger value as a boolean.

        {LAMP_REVIEW}
    """
    print_completion(prompt)

STORY = """
Text sample:
'''
In a recent survey conducted by the government, public sector employees were asked to rate their level 
of satisfaction with the department they work at. The results revealed that NASA was the most popular 
department with a satisfaction rating of 95%.

One NASA employee, John Smith, commented on the findings, stating, "I'm not surprised that NASA came out on top. 
It's a great place to work with amazing people and incredible opportunities. I'm proud to be a part of 
such an innovative organization."

The results were also welcomed by NASA's management team, with Director Tom Johnson stating, "We are thrilled to 
hear that our employees are satisfied with their work at NASA. We have a talented and dedicated team who work tirelessly 
to achieve our goals, and it's fantastic to see that their hard work is paying off."

The survey also revealed that the Social Security Administration had the lowest satisfaction rating, with 
only 45% of employees indicating they were satisfied with their job. The government has pledged to address 
the concerns raised by employees in the survey and work towards improving job satisfaction across all departments.
'''
"""

def infer_5_topics():
    """Inferring topics"""
    prompt = f"""
        Determine five topics that are being discussed in the following text, which is delimited by triple backticks.
        Make each item one or two words long. 
        Format your response as a list of items separated by commas.

        {STORY}
    """
    response = get_completion(prompt)
    # print(response)

    topic_list = response.splitlines()
    for i, topic in enumerate(topic_list):
        topic_list[i] = topic[3:]

    print(', '.join(topic_list))

# sentiment()
# sentiment_one_word()
# identify_emotions()
# identify_item_and_company()
# identify_multiple_items()
infer_5_topics()
