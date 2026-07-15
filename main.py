from typing import List

from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool #c'est une fonction qu'un agent peut utiliser pour accomplir une tâche
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch



# from tavily import TavilyClient

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that serches over internet
#     Args:
#         query (str): The query to search for
#         Returns:
#             The search results
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)

class Source(BaseModel):
    """Schema for a source used b the agent"""
    url:str = Field(description="The URL of the source")
    
class AgentResponse(BaseModel):
    """Schema for agent with answer and"""
    answer:str = Field(description="The agent answer's to the query")
    sources:List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm= ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an devops or SRE engineer with ai skills  in France area on linkedin where applications are still open and list their details")})
    print(result)


if __name__ == "__main__":
    main()
