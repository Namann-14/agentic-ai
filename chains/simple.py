import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b')

prompt = PromptTemplate(
    template='Generate 5 interesting fact about this ${topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | llm | parser

res = chain.invoke({'topic': 'genichiro ashina'})

print(res)

chain.get_graph().print_ascii()