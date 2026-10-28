from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from termcolor import COLORS, colored
from random import choice

# Load environment variables
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

# Create the semantic chunker
chunker = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.1
)

# Split the text into semantic chunks
chunks = chunker.split_text(text)
print(chunks)


# Display chunks in different colors
def display_chunks(chunks):
    colors_list = list(COLORS.keys())[2:8]

    print(f"Total Number of Chunks: {len(chunks)}")

    for num, chunk in enumerate(chunks, 1):
        print(f"Chunk {num}: Length {len(chunk)} chars")
        print(
            colored(text=chunk, color=choice(colors_list)),
            end="\n\n"
        )


display_chunks(chunks)