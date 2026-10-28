import json
from pathlib import Path
from pprint import pp

from langchain_core.documents import Document

path = Path(__file__).parent / "books" / "apparels.json"
print(path.exists())

def metadata(record: dict) -> dict:
    return {
        "product_name": record['productName'],
        "category": record["category"],
        "price": record["price"]
    }

with path.open("r", encoding="utf-8") as f:
    data = json.load(f)

    documents = [
        Document(
            page_content=product["Description"],
            metadata={
                "source": str(path),
                **metadata(product)
            },
        )
        for product in data["products"]
    ]

for doc in documents:
    print(doc.page_content, end="\n\n")

if documents:
    pp(documents[0].metadata)

print("Total documents:", len(documents))