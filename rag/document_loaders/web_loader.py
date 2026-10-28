# 1. WebBaseLoader
from pprint import pp
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document

# 1. Define URLs
urls = [
    "https://namannayak.vercel.app/blog/lessons-from-an-associate-software-developer-internship",
]

# 2. Configure HTTP requests
session = requests.Session()

# 3. Load and parse each web page
documents = []

for url in urls:
    response = session.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    # Remove content that isn't useful as page text
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    title = soup.title.get_text(strip=True) if soup.title else ""

    main_content = soup.find("main") or soup.body or soup
    page_content = main_content.get_text(separator="\n", strip=True)

    documents.append(
        Document(
            page_content=page_content,
            metadata={
                "source": url,
                "title": title,
                "language": soup.html.get("lang", "") if soup.html else "",
            },
        )
    )

# 4. Inspect results
print("Documents:", len(documents))
print(documents[0].page_content)
pp(documents[0].metadata)
