"""Give the model time to “think”"""
from openai_wrapper import print_completion

TEXT = """
    In a charming village, siblings Jack and Jill set out on \\
    a quest to fetch water from a hilltop \\
    well. As they climbed, singing joyfully, misfortune \\
    struck—Jack tripped on a stone and tumbled \\
    down the hill, with Jill following suit. \\
    Though slightly battered, the pair returned home to \\
    comforting embraces. Despite the mishap, \\
    their adventurous spirits remained undimmed, and they \\
    continued exploring with delight.
"""

def tactic_1a():
    """Specify the steps required to complete a task"""
    prompt = f"""
        Perform the following actions: 
        1 - Summarize the following text delimited by triple \\
        backticks with 1 sentence.
        2 - Translate the summary into French.
        3 - List each name in the French summary.
        4 - Output a json object that contains the following \\
        keys: french_summary, num_names.

        Separate your answers with line breaks.

        Text:
        ```{TEXT}```
    """
    print_completion(prompt)

def tactic_1b():
    """Ask for output in a specified format"""
    prompt = f"""
        Your task is to perform the following actions: 
        1 - Summarize the following text delimited by 
        <> with 1 sentence.
        2 - Translate the summary into French.
        3 - List each name in the French summary.
        4 - Output a json object that contains the 
        following keys: french_summary, num_names.

        Use the following format:
        Text: <text to summarize>
        Summary: <summary>
        Translation: <summary translation>
        Names: <list of names in summary>
        Output JSON: <json with summary and num_names>

        Text: <{TEXT}>
    """
    print_completion(prompt)

QUESTION = """
    I'm building a solar power installation and I need help working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot
    What is the total cost for the first year of operations as a function of the number of square feet.
"""

STUDENT_SOLUTION = """
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""

def tactic_2a():
    """Incorrect answer"""
    prompt = f"""
        Determine if the student's solution is correct or not.

        Question:
        {QUESTION}

        Student's Solution:
        {STUDENT_SOLUTION}
        """
    print_completion(prompt)

def tactic_2b():
    """Instruct the model to work out its own solution before rushing to a conclusion"""
    prompt = f"""
        Your task is to determine if the student's solution is correct or not.
        To solve the problem do the following:
        - First, work out your own solution to the problem including the final total. 
        - Then compare your solution to the student's solution and evaluate if the student's solution is correct or not.
        - Don't decide if the student's solution is correct until you have done the problem yourself.

        Use the following format:
        Question:
        ```
        question here
        ```
        Student's solution:
        ```
        student's solution here
        ```
        Actual solution:
        ```
        steps to work out the solution and your solution here
        ```
        Is the student's solution the same as actual solution just calculated:
        ```
        yes or no
        ```
        Student grade:
        ```
        correct or incorrect
        ```

        Question:
        ```
        {QUESTION}
        ``` 
        Student's solution:
        ```
        {STUDENT_SOLUTION}
        ```
        Actual solution:
        """
    print_completion(prompt)

# tactic_1a()
# tactic_1b()
# tactic_2a()
tactic_2b()
