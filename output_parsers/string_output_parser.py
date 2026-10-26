from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

input_template = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
)

output_template = PromptTemplate(
    template="Write a 5 line summary on the following: {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = (
    input_template
    | llm
    | parser
    | RunnableLambda(lambda text: {"text": text})
    | output_template
    | llm
    | parser
)

res = chain.invoke({"topic": "black hole"})

print(res)