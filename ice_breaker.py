import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

information = """
Luiz Inácio Lula da Silva (nascido Luiz Inácio da Silva;[nota 2] Garanhuns,[nota 3] 27 de outubro de 1945), mais conhecido como Lula, é um ex-metalúrgico, ex-sindicalista e político brasileiro, filiado ao Partido dos Trabalhadores (PT). É o 39.º presidente do Brasil desde 2023, havendo sido também o 35.º a ocupar o cargo, entre 2003 e 2011.

De origem pobre, migrou ainda criança de Pernambuco para São Paulo com sua família. Foi metalúrgico e sindicalista, época em que recebeu a alcunha "Lula", forma hipocorística de "Luís". Durante a ditadura militar, liderou grandes greves de operários no ABC Paulista e ajudou a fundar o PT em 1980, durante o processo de abertura política. Lula foi uma das principais lideranças do movimento Diretas Já, no período da redemocratização, quando iniciou sua carreira política. Elegeu-se em 1986 deputado federal pelo estado de São Paulo com votação recorde. Em 1989 concorreu pela primeira vez à presidência da República, perdendo no segundo turno para Fernando Collor de Mello. Foi candidato a presidente por outras duas vezes, em 1994 e em 1998, perdendo ambas as eleições no primeiro turno para Fernando Henrique Cardoso. Venceu a eleição presidencial de 2002, derrotando José Serra no segundo turno. Na eleição de 2006, foi reeleito ao superar Geraldo Alckmin no segundo turno.

O governo Lula teve como marco a consolidação de programas sociais como o Bolsa Família e o Fome Zero, ambos reconhecidos pela Organização das Nações Unidas como iniciativas que possibilitaram a saída do país do mapa da fome. Durante seus dois mandatos, empreendeu reformas e mudanças radicais que produziram transformações sociais e econômicas no Brasil, que acumulou substanciais reservas internacionais, triplicou seu PIB per capita e alcançou o grau de investimento. Os índices de pobreza, desigualdade, analfabetismo, desemprego, mortalidade infantil e trabalho infantil caíram significativamente, enquanto o salário mínimo e a renda média do trabalhador tiveram ganhos reais e o acesso à escola, à universidade e ao atendimento de saúde se expandiram. Na política externa, desempenhou um papel de destaque, incluindo atividades relacionadas ao programa nuclear do Irã, ao aquecimento global, ao Mercosul e aos BRICS. Lula foi considerado um dos políticos mais populares da história do Brasil e, enquanto presidente, foi um dos mais populares do mundo. Foi sucedido no cargo pela chefe da Casa Civil no seu governo, Dilma Rousseff, eleita em 2010 e reeleita em 2014.

Após a presidência, Lula manteve-se ativo no cenário político e passou a ministrar palestras no Brasil e no exterior. Candidatou-se à presidência nas eleições de 2018, mas teve a sua candidatura indeferida por ser condenado à prisão no âmbito da Operação Lava Jato, em um julgamento controverso. Em 2019, foi liberto com base em decisão do Supremo Tribunal Federal, que anulou paulatinamente suas condenações. Com seus direitos políticos restituídos, candidatou-se à presidência pela sexta vez nas eleições de 2022 e, ao vencer Jair Bolsonaro no segundo turno, tornou-se a primeira pessoa a derrotar um presidente brasileiro candidato à reeleição e o primeiro a se tornar presidente pela terceira vez.
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
    # llm = ChatOpenAI(
    #     temperature=0,
    #     model_name="text-moderation-stable",
    # )
    llm = ChatOllama(model="llama3.2")
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})
    print(res)
