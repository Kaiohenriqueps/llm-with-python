# python imports
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile

# langchain imports
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def ice_break_with(name: str) -> str:
    linkedin_username = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
    given the LinkedIn information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting factor about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOllama(model="llama3.2")
    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": linkedin_data})
    print(res)


if __name__ == "__main__":
    load_dotenv()
    print("ICE BREAKER!")
    ice_break_with(name="Kaio Henrique Pedroza Silva")
