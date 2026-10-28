import os

from pathlib import Path
from langchain_core.documents import Document
from pprint import pp

path = Path().cwd() / "books" / "transformers.txt"
print(path.exists())

with path.open("r", newline="", encoding="utf-8", errors="replace") as f:
    text = f.read()

    documents = [
        Document(
            page_content=text,
            metadata={
                "source": str(path)
            }
        )
    ]

print(type(documents))
print(type(documents[0]))
print(len(documents))  
pp(documents[0].metadata)  

