import os
from dotenv import load_dotenv

from huggingface_hub import notebook_login
from smolagents import CodeAgent, tool, DuckDuckGoSearchTool, HfApiModel

load_dotenv()

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu base on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."







# os.environ["HF_TOKEN"] = dotenv.
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

# agent.run("Search for the best music recommendation for a party at the Wayne's mansion.")
agent.run(input("Quesiton: "))

