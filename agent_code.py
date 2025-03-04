import os
from dotenv import load_dotenv

from huggingface_hub import notebook_login
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

load_dotenv()

# os.environ["HF_TOKEN"] = dotenv.
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

# agent.run("Search for the best music recommendation for a party at the Wayne's mansion.")
agent.run(input("Quesiton: "))

