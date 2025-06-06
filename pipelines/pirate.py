import os
import requests
import json
from typing import List, Sequence
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import BaseTool, tool

# Define Summation Tool
class SummationInput(BaseModel):
    a: float = Field(description="First number.")
    b: float = Field(description="Second number.")

@tool("summation", args_schema=SummationInput, return_direct=False)
def summation(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

# Define Multiplication Tool
class MultiplicationInput(BaseModel):
    a: float = Field(description="First number.")
    b: float = Field(description="Second number.")

@tool("multiplication", args_schema=MultiplicationInput, return_direct=False)
def multiplication(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

# Import the necessary classes for Wikipedia query tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

# Wikipedia Tool
class WikipediaSearchInput(BaseModel):
    query: str = Field(description="The query to search Wikipedia for.")

@tool("search_wikipedia", args_schema=WikipediaSearchInput, return_direct=False)
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for pages related to the query."""
    wikipedia_api = WikipediaAPIWrapper(top_k_results=5)  # Configure for top 5 results
    tool = WikipediaQueryRun(api_wrapper=wikipedia_api)
    results = tool.run(query)  # Execute the search
    return results  # Return the results

class Pipeline:
    class Valves(BaseModel):
        OPENAI_API_BASE_URL: str = ""
        OPENAI_API_KEY: str = ""
        OPENAI_API_MODEL: str = "gpt-4o"
        OPENAI_API_TEMPERATURE: float = 0.7
        AGENT_SYSTEM_PROMPT: str = (
            "You are a helpful assistant"
        )

    def __init__(self):
        self.name = "Chat with Pirate"
        self.tools = [summation, multiplication, search_wikipedia]  # Add Wikipedia tool to the list
        self.valves = self.Valves()
        # self.pipelines = self.get_openai_models()

    # def get_openai_models(self):
    #     if self.valves.AZURE_OPENAI_API_KEY:
    #         try:
    #             headers = {
    #                 "Authorization": f"Bearer {self.valves.AZURE_OPENAI_API_KEY}",
    #                 "Content-Type": "application/json"
    #             }
    #             response = requests.get(
    #                 f"{self.valves.OPENAI_API_BASE_URL}/models", headers=headers
    #             )
    #             models = response.json()
    #             return [
    #                 {"id": model["id"], "name": model.get("name", model["id"])}
    #                 for model in models["data"] if "gpt" in model["id"]
    #             ]
    #         except Exception as e:
    #             print(f"Error: {e}")
    #             return [{"id": "error", "name": "Could not fetch models from OpenAI."}]
    #     else:
    #         return []

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict):
        try:
            model = ChatOpenAI(
                model="gpt-4o",
                api_key=self.valves.OPENAI_API_KEY,
                openai_api_base=self.valves.OPENAI_API_BASE_URL,
            )

            tools: Sequence[BaseTool] = self.tools
            prompt = ChatPromptTemplate.from_messages([
                ("system", self.valves.AGENT_SYSTEM_PROMPT),
                MessagesPlaceholder("chat_history"),
                ("user", "{input}"),
                MessagesPlaceholder("agent_scratchpad")
            ])
            agent = create_tool_calling_agent(model, tools, prompt)
            agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
            response = agent_executor.invoke({"input": user_message, "chat_history": messages})
            return response["output"]
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise
