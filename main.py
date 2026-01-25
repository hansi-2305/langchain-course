
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from langchain_tavily import TavilySearch

# from tavily import TavilyClient

# tavily = TavilyClient()

# @tool
# def search(query: str)->str:
#     """
#     Tool that searches over internet 
#     Args:
#        quey: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)

llm = ChatOllama(model="qwen2.5:3b")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from lang-chain course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job posting for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main() 