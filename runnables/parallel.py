import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b')

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {game}',
    input_variables=['game']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, llm, parser),
    'linkedin': RunnableSequence(prompt2, llm, parser)
})

res = parallel_chain.invoke({
    'topic': 'genichiri ashina (sekiro)',
    'game': 'gow 2018'
})

print(res['tweet'])
print(res['linkedin'])

parallel_chain.get_graph().print_ascii()