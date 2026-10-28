import csv

from pprint import pp
from pathlib import Path
from langchain_core.documents import Document

path = Path().cwd() / "books" / "organizations.csv"
print("Path exists: ",path.exists())

with path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    documents = [
        Document(
            page_content=(
                f"Name: {row['Name']}\n"
                f"Industry: {row['Industry']}\n"
                f"Country: {row['Country']}\n"
                f"Founded: {row['Founded']}\n"
                f"Description: {row['Description']}"
            ),
            metadata={
                "source": row["Industry"],
                "row": i,
                "Website": row["Website"],
                "Founded": row["Founded"],
                "Number of employees": row["Number of employees"]
            }
        )
        for i, row in enumerate(reader)
    ]
# for i in range(1, 10):
#     print(documents[i])
print(type(documents[0]))
pp(documents[0].metadata)