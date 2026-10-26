import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

input_template = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

output_template = PromptTemplate(
    template="Write a 5 line summary on the following: {text}",
    input_variables=['text']
)

prompt1 = input_template.invoke({'topic': 'black hole'})  
res1 = llm.invoke(prompt1)

prompt2 = output_template.invoke({'text': res1.content})
res2 = llm.invoke(prompt2)  

print(res2.content)