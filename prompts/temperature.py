import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not set.")

llm1 = ChatGroq(model="openai/gpt-oss-20b", temperature=1.5)
llm2 = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

response = llm1.invoke("Write me a haiku on autumn.")
response2 = llm2.invoke("Write me a haiku on autumn.")

print(response.content)
print("==========")
print(response2.content)