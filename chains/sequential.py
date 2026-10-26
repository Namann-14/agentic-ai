import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b')

prompt1 = PromptTemplate(
    template='Generate a detailed report on topic: ${topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 line summary on this text: ${text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | llm | parser | RunnableLambda(lambda text: {'text': text}) | prompt2 | llm | parser

res = chain.invoke({
    'topic': 'genichiro ashina'
})

print(res)