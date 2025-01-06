# python imports
import os
from dotenv import load_dotenv

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
            name="Crawl Google 4 linekdin profile page",
            func="",
            description="useful for when you need to get the Linkedin Page URL",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Kaio Henrique Pedroza Silva")
    print(linkedin_url)
