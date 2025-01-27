from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()


def get_profile_url_tavily(name: str):
    """Searches for LinkedIn Profile page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res
