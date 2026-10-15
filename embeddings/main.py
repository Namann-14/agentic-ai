import os

import numpy as np
from dotenv import load_dotenv
from langchain_community.embeddings import JinaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

if not os.getenv("JINA_API_KEY"):
    raise RuntimeError("JINA_API_KEY is not set in the environment or .env file.")

embeddings = JinaEmbeddings(session=None)

documents = [
    "LangChain helps developers build applications powered by language models.",
    "The weather is sunny and warm today.",
    "Embeddings represent text as vectors for semantic search.",
]

query = "How can I search text by meaning?"

document_vectors = embeddings.embed_documents(documents)
query_vector = embeddings.embed_query(query)
similarities = cosine_similarity(
    np.asarray([query_vector]),
    np.asarray(document_vectors),
)[0]

ranked_documents = sorted(
    zip(similarities, documents),
    key=lambda item: item[0],
    reverse=True,
)

print(f"Query: {query}\n")
for score, document in ranked_documents:
    print(f"{score:.3f}  {document}")