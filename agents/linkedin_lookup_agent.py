# python imports
from dotenv import load_dotenv
from custom_tools.tools import get_profile_url_tavily

# langchain imports
from langchain import hub
from langchain_core.tools import Tool
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOllama(model="llama3.2")
    template = """given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
    Your answer should contain only a URL."""
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Linkedin Page URL",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(
        agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True
    )
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]
    return linkedin_profile_url
