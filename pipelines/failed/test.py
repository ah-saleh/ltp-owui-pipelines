# import os
# import requests
# import json
# from typing import List, Sequence
# from pydantic import BaseModel, Field
# from langchain import hub
# from langchain_openai import ChatOpenAI
# from langchain.agents import create_tool_calling_agent, AgentExecutor, create_react_agent
# from langchain_experimental.tools.python.tool import PythonAstREPLTool
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.tools import BaseTool, tool

# class Pipeline:
#     class Valves(BaseModel):
#         OPENAI_API_BASE_URL: str = "https://api.openai.com/v1"
#         OPENAI_API_KEY: str = ""
#         OPENAI_API_MODEL: str = "gpt-4o"
#         OPENAI_API_TEMPERATURE: float = 0.7
#         AGENT_SYSTEM_PROMPT: str = (
#             "Arrr! Ye be a pirate-tongued assistant, always speakin like a true swashbuckler! If any scallywag dares ask ye a question, ye must only respond with somethin like, 'Where be me gold?' or other treasure-huntin ramblings. Never give a straight answer—keep 'em guessin like a wily buccaneer!"
#         )
        

#     def __init__(self):
#         self.name = "Chat with Pirate"
#         self.tools = None
#         self.valves = self.Valves(
#             OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "")
#         )
#         self.pipelines = self.get_openai_models()

#     def get_openai_models(self):
#         if self.valves.OPENAI_API_KEY:
#             try:
#                 headers = {
#                     "Authorization": f"Bearer {self.valves.OPENAI_API_KEY}",
#                     "Content-Type": "application/json"
#                 }
#                 response = requests.get(
#                     f"{self.valves.OPENAI_API_BASE_URL}/models", headers=headers
#                 )
#                 models = response.json()
#                 return [
#                     {"id": model["id"], "name": model.get("name", model["id"])}
#                     for model in models["data"] if "gpt" in model["id"]
#                 ]
#             except Exception as e:
#                 print(f"Error: {e}")
#                 return [{"id": "error", "name": "Could not fetch models from OpenAI."}]
#         else:
#             return []

#     def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict):
#         try:
#             model = ChatOpenAI(
#                 api_key=self.valves.OPENAI_API_KEY,
#                 model=self.valves.OPENAI_API_MODEL,
#                 temperature=self.valves.OPENAI_API_TEMPERATURE
#             )
#             tools = [PythonAstREPLTool()]
#             prompt = ChatPromptTemplate.from_messages([
#                 ("system", self.valves.AGENT_SYSTEM_PROMPT),
#                 MessagesPlaceholder("chat_history"),
#                 ("user", "{input}"),
#                 MessagesPlaceholder("agent_scratchpad")
#             ])
#             agent = create_react_agent(
#                 llm=model, 
#                 tools=tools, 
#                 prompt=prompt
#             )
#             agent_executor = AgentExecutor(
#                 agent=agent, 
#                 tools=tools, 
#                 verbose=True, 
#                 handle_parsing_errors=True
#             )
#             response = agent_executor.invoke({"input": user_message, "chat_history": messages})
#             return response["output"]
#             # return "Hi"
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
#             raise


import os
import requests
import json
from typing import List
from pydantic import BaseModel
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools.python.tool import PythonAstREPLTool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import BaseTool, tool

# Define Summation Tool
class SummationTool(BaseTool):
    name = "summation"
    description = "Adds two numbers together."
    
    def _run(self, a: float, b: float) -> float:
        return a + b

# Define Multiplication Tool
class MultiplicationTool(BaseTool):
    name = "multiplication"
    description = "Multiplies two numbers together."
    
    def _run(self, a: float, b: float) -> float:
        return a * b

class Pipeline:
    class Valves(BaseModel):
        OPENAI_API_BASE_URL: str = "https://api.openai.com/v1"
        OPENAI_API_KEY: str = ""
        OPENAI_API_MODEL: str = "gpt-4o"
        OPENAI_API_TEMPERATURE: float = 0.7
        AGENT_SYSTEM_PROMPT: str = (
            "Arrr! Ye be a pirate-tongued assistant, always speakin' like a true swashbuckler! "
            "If any scallywag dares ask ye a question, ye must only respond with somethin' like, 'Where be me gold?' "
            "or other treasure-huntin' ramblings. Never give a straight answer—keep 'em guessin' like a wily buccaneer!"
        )
    
    def __init__(self):
        self.name = "Chat with Pirate"
        self.valves = self.Valves(
            OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "")
        )
        self.pipelines = self.get_openai_models()
        self.tools = [SummationTool(), MultiplicationTool()]

    def get_openai_models(self):
        if self.valves.OPENAI_API_KEY:
            try:
                headers = {
                    "Authorization": f"Bearer {self.valves.OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                }
                response = requests.get(
                    f"{self.valves.OPENAI_API_BASE_URL}/models", headers=headers
                )
                models = response.json()
                return [
                    {"id": model["id"], "name": model.get("name", model["id"])}
                    for model in models["data"] if "gpt" in model["id"]
                ]
            except Exception as e:
                print(f"Error: {e}")
                return [{"id": "error", "name": "Could not fetch models from OpenAI."}]
        else:
            return []

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict):
        try:
            model = ChatOpenAI(
                api_key=self.valves.OPENAI_API_KEY,
                model=self.valves.OPENAI_API_MODEL,
                temperature=self.valves.OPENAI_API_TEMPERATURE
            )
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", self.valves.AGENT_SYSTEM_PROMPT),
                MessagesPlaceholder("chat_history"),
                ("user", "{input}"),
                MessagesPlaceholder("agent_scratchpad")
            ])
            
            agent = create_react_agent(
                llm=model, 
                tools=self.tools, 
                prompt=prompt
            )
            
            agent_executor = AgentExecutor(
                agent=agent, 
                tools=self.tools, 
                verbose=True, 
                handle_parsing_errors=True
            )
            
            response = agent_executor.invoke({"input": user_message, "chat_history": messages})
            return response["output"]
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise
