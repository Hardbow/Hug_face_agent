from smolagents import load_tool, CodeAgent, HfApiModel
from dotenv import load_dotenv
import time

load_dotenv()
image_generation_tool = load_tool(
    "m-ric/text-to-image",
    trust_remote_code=True
)

agent = CodeAgent(
    tools=[image_generation_tool],
    model=HfApiModel()
)

agent.run("Generate an image of a luxurious superhero-themed party at Wayne Manor with made-up superheros.")
time.sleep(15)

# import os
# from dotenv import load_dotenv
# from smolagents import Tool, CodeAgent, HfApiModel
#
# load_dotenv()
# os.environ["PYTHONIOENCODING"] = 'utf-8'
# print(os.getenv("PYTHONIOENCODING"))
#
# class SuperheroPartyThemeTool(Tool):
#     name = "superhero_party_theme_generator"
#     description = """
#     This tool suggests creative superhero-themed party ideas based on a category.
#     It returns a unique party theme idea."""
#
#     inputs = {
#         "category": {
#             "type": "string",
#             "description": "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic gotham').",
#         }
#     }
#
#     output_type = "string"
#
#     def forward(self, category: str):
#         themes = {
#             "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
#             "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
#             "futuristic gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets."
#         }
#
#         return themes.get(category.lower(),
#                           "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.")
#
#
# # Instantiate the tool
# party_theme_tool = SuperheroPartyThemeTool()
# agent = CodeAgent(tools=[party_theme_tool], model=HfApiModel())
#
# # Run the agent to generate a party theme idea
# # result = agent.run(
# #     "What would be a good superhero party idea for a 'villain masquerade' theme?"
# # )
#
# party_theme_tool.push_to_hub("YouGene/party_theme_tool", token="")
#
# # print(result)