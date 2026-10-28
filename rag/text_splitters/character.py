from langchain_text_splitters import CharacterTextSplitter
from termcolor import colored, COLORS
from random import choice
from langchain_core.documents import Document
from pprint import pp

def display(chunks):
    colors_list = list(COLORS.keys())[2:8]
    print(f"Total chunks: {len(chunks)}")

    for num, chunk in enumerate(chunks, 1):
        print(f"Chunk {num}: Length {len(chunk)} chars")
        print(
            colored(text=chunk, color=choice(colors_list)),
            end="\n\n"
        )

text = """Artificial intelligence is transforming technology and shaping the future.
Machine learning algorithms are becoming more sophisticated every day.
Deep learning models can now process vast amounts of data efficiently.

Natural language processing has made significant strides in recent years.
Computer vision systems can now identify objects with remarkable accuracy.
Reinforcement learning is enabling robots to learn complex tasks autonomously.

The impact of AI extends across multiple industries including healthcare, finance, and transportation.
Ethical considerations around AI development are becoming increasingly important.
Researchers are working on making AI systems more transparent and explainable."""

# splitter = CharacterTextSplitter(
#     separator="",
#     chunk_size=100,
#     chunk_overlap=0,
#     length_function=len,    
# )

# chunk = splitter.split_text(text)

# display(chunk)

def create_chunks(
        text: str,
        chunk_size: int,
        seperator: str,
        chunk_overlap: int = 0
) -> list[str]:
    splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separator=seperator
    )

    chunks = splitter.split_text(text)
    return chunks

display(create_chunks(text, 150, " "))

display(create_chunks(text, 100, "\n\n"))