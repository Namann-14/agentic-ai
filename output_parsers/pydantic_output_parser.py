from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

input_prompt = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person\n{format_instruction}",
    input_variables=["place"],
    partial_variables={
        "format_instruction": parser.get_format_instructions(),
    },
)

chain = input_prompt | llm | parser

res = chain.invoke({"place": "Shibuya"})

print(res)