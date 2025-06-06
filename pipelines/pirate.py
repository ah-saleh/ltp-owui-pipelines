import os
from typing import List, Sequence, Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool, BaseTool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.chat_models import ChatOpenAI  # works with custom base URLs
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun


# # Define a summation tool
# class SummationInput(BaseModel):
#     a: float = Field(description="First number.")
#     b: float = Field(description="Second number.")


# @tool("summation", args_schema=SummationInput, return_direct=False)
# def summation(a: float, b: float) -> float:
#     """Adds two numbers together."""
#     return a + b


# # Define a multiplication tool
# class MultiplicationInput(BaseModel):
#     a: float = Field(description="First number.")
#     b: float = Field(description="Second number.")


# @tool("multiplication", args_schema=MultiplicationInput, return_direct=False)
# def multiplication(a: float, b: float) -> float:
#     """Multiplies two numbers together."""
#     return a * b


# # Define a Wikipedia search tool
# class WikipediaSearchInput(BaseModel):
#     query: str = Field(description="The query to search Wikipedia for.")


# @tool("search_wikipedia", args_schema=WikipediaSearchInput, return_direct=False)
# def search_wikipedia(query: str) -> str:
#     """Search Wikipedia for pages related to the query."""
#     wikipedia_api = WikipediaAPIWrapper(top_k_results=3)
#     wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia_api)
#     return wiki_tool.run(query)


# OpenWebUI pipeline
class Pipeline:
    class Valves(BaseModel):
        OPENAI_API_KEY: str = ''
        OPENAI_API_BASE_URL: str = ''
        OPENAI_API_TEMPERATURE: str = '0.7'
        AGENT_SYSTEM_PROMPT: str = "You are a helpful assistant. Use tools if needed."

    def __init__(self):
        self.name = "LangChain Agent with Tools"
        self.valves = self.Valves()
        #self.tools: Sequence[BaseTool] = [summation, multiplication, search_wikipedia]

    #     self.agent_executor: Optional[AgentExecutor] = None
    #     self._setup_agent()

    # def _setup_agent(self):
    #     model = ChatOpenAI(
    #         model=self.valves.OPENAI_API_MODEL,
    #         temperature=self.valves.OPENAI_API_TEMPERATURE,
    #         api_key=self.valves.OPENAI_API_KEY,
    #         base_url=self.valves.OPENAI_API_BASE_URL,
    #     )

    #     prompt = ChatPromptTemplate.from_messages([
    #         ("system", self.valves.AGENT_SYSTEM_PROMPT),
    #         MessagesPlaceholder("chat_history"),
    #         ("user", "{input}"),
    #         MessagesPlaceholder("agent_scratchpad")
    #     ])

    #     agent = create_tool_calling_agent(llm=model, tools=self.tools, prompt=prompt)

    #     self.agent_executor = AgentExecutor(
    #         agent=agent,
    #         tools=self.tools,
    #         verbose=True,
    #         handle_parsing_errors=True
    #     )

    async def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> dict:
        try:
            # result = self.agent_executor.invoke({
            #     "input": user_message,
            #     "chat_history": messages,
            # })
            return {"output": "Hello World!"}  # OpenWebUI expects this format
        except Exception as e:
            return {"output": f"An error occurred: {str(e)}"}
