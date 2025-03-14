import numpy as np
import time
import datetime
from dotenv import load_dotenv

from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, tool


@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party (casual, formal or superhero)
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == 'formal':
        return "3-course dinner with wine and dessert"
    elif occasion == 'superhero':
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."


load_dotenv()

agent = CodeAgent(tools=[], model=HfApiModel(), additional_authorized_imports=['datatime'])
# agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())
# agent.run("Prepare a formal menu for the party")
# agent.run("Search for the top 5 best movie of New wave")
agent.run(
    """"
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """
)
