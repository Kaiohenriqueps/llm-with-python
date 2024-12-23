import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

information = """
Luiz Inácio Lula da Silva (nascido Luiz Inácio da Silva;[nota 2] Garanhuns,[nota 3] 27 de outubro de 1945), mais conhecido como Lula, é um ex-metalúrgico, ex-sindicalista e político brasileiro, filiado ao Partido dos Trabalhadores (PT). É o 39.º presidente do Brasil desde 2023, havendo sido também o 35.º a ocupar o cargo, entre 2003 e 2011.
"""

if __name__ == "__main__":
    load_dotenv()
    print("Hello, Langchain!")

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting factor about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(
        temperature=0,
        model_name="text-moderation-stable",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})
    print(res)
