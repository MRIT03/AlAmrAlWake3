import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def extract_with_tavily(url):
    result = tavily.extract(urls=[url])
    return result[0]

# def query_tavily(query, max_results=10):
#     if not TAVILY_API_KEY:
#         raise EnvironmentError("TAVILY_API_KEY not found in environment variables.")
    
#     url = "https://api.tavily.com/search"
#     headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
#     payload = {
#         "query": query,
#         "max_results": max_results,
#         "include_answer": False,
#         "include_raw_content": True,
#     }

#     response = requests.post(url, headers=headers, json=payload)
#     response.raise_for_status()

#     return response.json()["results"]

