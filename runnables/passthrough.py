# RunnablePassthrough is like a pipe that passes your input forward without changing it.
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b')

prompt = PromptTemplate(
    template="write a short note on topic: \n ${topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following topic - {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt, llm, parser)

parallel_chain = RunnableParallel({
    'topic': RunnablePassthrough(),
    'explain': RunnableSequence(prompt2, llm, parser)
})

final = RunnableSequence(chain, parallel_chain)

res = final.invoke({
    'topic': 'genichiro ashina (sekiro)'
})

print(res)

final.get_graph().print_ascii()


