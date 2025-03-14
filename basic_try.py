import numpy as np
import time
import datetime
from dotenv import load_dotenv

from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, FinalAnswerTool, HfApiModel, Tool, tool, VisitWebpageTool
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

os.environ["PYTHONIOENCODING"] = 'utf-8'





load_dotenv()

# agent = CodeAgent(tools=[], model=HfApiModel(), additional_authorized_imports=['datatime'])
# agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())
# agent.run("Prepare a formal menu for the party")
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())
agent.run("Search for the top 5 best movie of New wave")
# agent.run(
#     """"
#     Alfred needs to prepare for the party. Here are the tasks:
#     1. Prepare the drinks - 30 minutes
#     2. Decorate the mansion - 60 minutes
#     3. Set up the menu - 45 minutes
#     4. Prepare the music and playlist - 45 minutes
#
#     If we start right now, at what time will the party be ready?
#     """
# )

agent.push_to_hub('YouGene/AlfredAgent')