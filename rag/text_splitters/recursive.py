from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from termcolor import COLORS, colored
from random import choice

text = """Hi how are you
My name is Genichiro Ashina

I am teaching RAG
We are Learning about RAG"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(chunks)


list_of_text = [text]

docs = [
    Document(page_content=content)
    for content in list_of_text
]

print(docs)


# Split the documents
chunks_docs = splitter.split_documents(docs)

print(chunks_docs)
print(len(chunks_docs))