import os
import requests
import json
from typing import List, Sequence
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import BaseTool, tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

from logging import getLogger
logger = getLogger(__name__)
logger.setLevel("DEBUG")


@tool("summation", return_direct=False)
def summation(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b


@tool("multiplication",return_direct=False)
def multiplication(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b


@tool("search_wikipedia", return_direct=False)
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for pages related to the query."""
    wikipedia_api = WikipediaAPIWrapper(top_k_results=5)  # Configure for top 5 results
    tool = WikipediaQueryRun(api_wrapper=wikipedia_api)
    results = tool.run(query)  # Execute the search
    return results  # Return the results


class Pipeline:

    class Valves(BaseModel):
        # OPENAI_API_KEY: str = Field(default="", description="OpenAI API key")
        # RATE_LIMIT: int = Field(default=5, description="Rate limit for the pipeline")
        # WORD_LIMIT: int = Field(default=300, description="Word limit when getting page summary")
        # WIKIPEDIA_ROOT: str = Field(default="https://en.wikipedia.org/wiki", description="Wikipedia root URL")
        OPENAI_API_BASE_URL: str = ""#os.getenv("URL", "")
        AZURE_OPENAI_API_KEY: str = ""
        OPENAI_API_MODEL: str = "gpt-4o"
        OPENAI_API_TEMPERATURE: float = 0.7
        AGENT_SYSTEM_PROMPT: str = (
            "You are a helpful assistant"
        )

    def __init__(self):
        # Optionally, you can set the id and name of the pipeline.
        # Best practice is to not specify the id so that it can be automatically inferred from the filename, so that users can install multiple versions of the same pipeline.
        # The identifier must be unique across all pipelines.
        # The identifier must be an alphanumeric string that can include underscores or hyphens. It cannot contain spaces, special characters, slashes, or backslashes.
        # self.id = "wiki_pipeline"
        self.name = "Test Pipeline"

        # Initialize valve paramaters
        # self.valves = self.Valves(
        #     **{k: os.getenv(k, v.default) for k, v in self.Valves.model_fields.items()}
        # )

        self.valves = self.Valves()

        self.tools = [summation, multiplication, search_wikipedia]

    async def on_startup(self):
        # This function is called when the server is started.
        logger.debug(f"on_startup:{self.name}")
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        logger.debug(f"on_shutdown:{self.name}")
        pass

    def pipe(
        self, 
        user_message: str, 
        model_id: str, 
        messages: List[dict], 
        body: dict
    ):
        
        try:
            model = AzureChatOpenAI(
                azure_deployment="gpt-4o",
                api_key=self.valves.AZURE_OPENAI_API_KEY,#os.getenv("AZURE_AZURE_OPENAI_API_KEY"),
                azure_endpoint="https://the-labs.openai.azure.com",
                api_version="2024-10-21",
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