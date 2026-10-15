import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

load_dotenv()

prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("chat_history"),
    ("human", "{question}"),
])

llm = ChatGroq(model="openai/gpt-oss-20b")

chain = prompt | llm

history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in {'exit', 'quit'}:
        break

    res = chain.invoke({
        "chat_history": history,
        "question": user_input
    })

    history.append(HumanMessage(user_input))
    history.append(AIMessage(res.content))

    history = history[-10:]
    
    print("AI: ", res.content)
