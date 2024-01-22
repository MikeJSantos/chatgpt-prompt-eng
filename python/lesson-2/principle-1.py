"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/2/guidelines"""
from varname import nameof
from get_completion import get_completion

def tactic_1():
    """ Use delimiters to clearly indicate distinct parts of the input"""
    text = """
        You should express what you want a model to do by \\\
        providing instructions that are as clear and \\\
        specific as you can possibly make them. \\\
        This will guide the model towards the desired output, \\\
        and reduce the chances of receiving irrelevant \\\
        or incorrect responses. Don't confuse writing a \\\
        clear prompt with writing a short prompt. \\\
        In many cases, longer prompts provide more clarity \\\
        and context for the model, which can lead to \\\
        more detailed and relevant outputs.
        """
    return f"""
        Summarize the text delimited by triple backticks \\
        into a single sentence.
        ```{text}```
        """

def tactic_2():
    """Ask for a structured output"""
    return """
        Generate a list of three made-up book titles along \\
        with their authors and genres. 
        Provide them in JSON format with the following keys: 
        book_id, title, author, genre.
        """

def tactic_3(text):
    """Ask the model to check whether conditions are satisfied"""
    return f"""
        You will be provided with text delimited by triple quotes. 
        If it contains a sequence of instructions, \\
        re-write those instructions in the following format:

        Step 1 - ...
        Step 2 - …
        …
        Step N - …

        If the text does not contain a sequence of instructions, \\
        then simply write \"No steps provided.\"

        \"\"\"{text}\"\"\"
        """

def tactic_3a():
    """Ask the model to check whether conditions are satisfied"""
    text = """
        Making a cup of tea is easy! First, you need to get some \\
        water boiling. While that's happening, \\
        grab a cup and put a tea bag in it. Once the water is \\
        hot enough, just pour it over the tea bag. \\
        Let it sit for a bit so the tea can steep. After a \\
        few minutes, take out the tea bag. If you \\
        like, you can add some sugar or milk to taste. \\
        And that's it! You've got yourself a delicious \\
        cup of tea to enjoy.
        """
    return tactic_3(text)

def tactic_3b():
    """\"No steps provided.\""""
    text = """
        The sun is shining brightly today, and the birds are \\
        singing. It's a beautiful day to go for a \\
        walk in the park. The flowers are blooming, and the \\
        trees are swaying gently in the breeze. People \\
        are out and about, enjoying the lovely weather. \\
        Some are having picnics, while others are playing \\
        games or simply relaxing on the grass. It's a \\
        perfect day to spend time outdoors and appreciate the \\
        beauty of nature.
        """
    return tactic_3(text)

def tactic_4():
    """\"Few-shot\" prompting"""
    return """
        Your task is to answer in a consistent style.

        <child>: Teach me about patience.

        <grandparent>: The river that carves the deepest \ 
        valley flows from a modest spring; the \ 
        grandest symphony originates from a single note; \ 
        the most intricate tapestry begins with a solitary thread.

        <child>: Teach me about resilience.
        """

print(f"""\n{nameof(tactic_1)}:\n\n{get_completion(tactic_1())}""")
print(f"""\n{nameof(tactic_2)}:\n\n{get_completion(tactic_2())}""")
print(f"""\n{nameof(tactic_3a)}:\n\n{get_completion(tactic_3a())}""")
print(f"""\n{nameof(tactic_3b)}:\n\n{get_completion(tactic_3b())}""")
print(f"""\n{nameof(tactic_4)}:\n\n{get_completion(tactic_4())}""")