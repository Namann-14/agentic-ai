# This is the base concept: chaining steps together with RunnableSequence.
# It shows the simplest mental model: prompt -> model -> parser -> next prompt -> model -> parser.

import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b')

prompt = PromptTemplate(
    template="Write a short note on topic: \n {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt, llm, parser)

res = chain.invoke({
    'topic': 'genichiro ashina (sekiro)'
})

print(res)

chain.get_graph().print_ascii() 