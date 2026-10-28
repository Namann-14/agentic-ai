
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from termcolor import colored, COLORS
from random import choice

load_dotenv()

text = """Artificial intelligence is transforming technology and shaping the future.
Machine learning algorithms are becoming more sophisticated every day.
Deep learning models can now process vast amounts of data efficiently.
Neural networks are inspired by the human brain's structure.

The best pasta recipes include fresh ingredients and proper cooking techniques.
Italian cuisine emphasizes quality olive oil and regional cheeses.
Authentic carbonara uses guanciale, eggs, pecorino romano, and black pepper.
Cooking pasta al dente ensures the best texture and flavor.

Climate change is affecting ecosystems worldwide.
Rising temperatures are causing glaciers to melt at unprecedented rates.
Scientists warn that immediate action is needed to reduce carbon emissions.
Renewable energy sources offer hope for a sustainable future."""

class Chunks(BaseModel):
    chunks: str = Field(description="")
    summary: str = Field(description="")

class Chunker(BaseModel):
    chunks: list[Chunks] = Field(description="")

llm = ChatGroq(model="openai/gpt-oss-20b")

splitter = llm.with_structured_output(
    schema=Chunker
)

prompt = ChatPromptTemplate(
    messages=[
        (
            "system",
            """You are an expert text chunker that splits the given text into a list of chunks. Understand the natural topic boundaries of the text. Do not change, rewrite, or omit any existing text. Only split the text where appropriate. For each chunk, generate a 1-2 line summary."""
        ),
        (
            "human",
            "Split the given text into chunks.\nText: {text}"
        )
    ],
    input_variables=['text']
)

chain = prompt | llm 

res = chain.invoke({
    'text': text
})

print(res.content)