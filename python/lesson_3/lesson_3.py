"""https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/3/iterative"""
import inspect
import tempfile
import webbrowser
from openai_wrapper import get_completion, print_completion

FACT_SHEET_CHAIR = """OVERVIEW
    - Part of a beautiful family of mid-century inspired office furniture, 
    including filing cabinets, desks, bookcases, meeting tables, and more.
    - Several options of shell color and base finishes.
    - Available with plastic back and front upholstery (SWC-100) 
    or full upholstery (SWC-110) in 10 fabric and 6 leather options.
    - Base finish options are: stainless steel, matte black, 
    gloss white, or chrome.
    - Chair is available with or without armrests.
    - Suitable for home or business settings.
    - Qualified for contract use.

    CONSTRUCTION
    - 5-wheel plastic coated aluminum base.
    - Pneumatic chair adjust for easy raise/lower action.

    DIMENSIONS
    - WIDTH 53 CM | 20.87”
    - DEPTH 51 CM | 20.08”
    - HEIGHT 80 CM | 31.50”
    - SEAT HEIGHT 44 CM | 17.32”
    - SEAT DEPTH 41 CM | 16.14”

    OPTIONS
    - Soft or hard-floor caster options.
    - Two choices of seat foam densities: 
    medium (1.8 lb/ft3) or high (2.8 lb/ft3)
    - Armless or 8 position PU armrests 

    MATERIALS
    SHELL BASE GLIDER
    - Cast Aluminum with modified nylon PA6/PA66 coating.
    - Shell thickness: 10 mm.
    SEAT
    - HD36 foam

    COUNTRY OF ORIGIN
    - Italy
"""

BASE_PROMPT = """
    Your task is to help a marketing team create a description for a retail website of a product based on a technical fact sheet.
    Write a product description based on the information provided in the technical specifications delimited by triple backticks.
"""

TECHNICAL_SPECIFICATIONS = f"""
    Technical specifications:
    ```
    {FACT_SHEET_CHAIR}
    ```
"""

def main():
    """Generate a marketing product description from a product fact sheet"""
    prompt = f"""
        {BASE_PROMPT}{TECHNICAL_SPECIFICATIONS}
    """
    print_completion(prompt)

def issue_1():
    """The text is too long"""
    prompt = f"""
        {BASE_PROMPT}    Use at most 50 words.\n{TECHNICAL_SPECIFICATIONS}
    """
    print_completion(prompt)

def issue_2():
    """Text focuses on the wrong details"""
    prompt = f"""
        Your task is to help a marketing team create a description for a retail website of a product based on a technical fact sheet.
        Write a product description based on the information provided in the technical specifications delimited by triple backticks.
        The description is intended for furniture retailers, so should be technical in nature and focus on the materials the product is constructed from.
        Use at most 50 words.
        {TECHNICAL_SPECIFICATIONS}
    """
    print_completion(prompt)

def issue_3():
    """Description needs a table of dimensions"""
    prompt = f"""
        Your task is to help a marketing team create a description for a retail website of a product based on a technical fact sheet.
        Write a product description based on the information provided in the technical specifications delimited by triple backticks.
        The description is intended for furniture retailers, so should be technical in nature and focus on the materials the product is constructed from.
        At the end of the description, include every 7-character Product ID in the technical specification.
        After the description, include a table that gives the product's dimensions. The table should have two columns.
        In the first column include the name of the dimension. 
        In the second column include the measurements in inches only.
        Give the table the title 'Product Dimensions'.
        Format everything as HTML that can be used in a website. 
        Place the description in a <div> element.
        {TECHNICAL_SPECIFICATIONS}
    """
    print(f"""\n{inspect.stack()[0][3]}():{prompt}""")
    html = get_completion(prompt)
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        url = 'file://' + f.name
        f.write(html)
    webbrowser.open(url)

# main()
# issue_1()
# issue_2()
issue_3()
