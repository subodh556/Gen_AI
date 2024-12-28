import warnings
from langchain._api import LangChainDeprecationWarning
from langchain_groq import ChatGroq

warnings.simplefilter("ignore",category=LangChainDeprecationWarning)

import os
from dotenv import load_dotenv , find_dotenv
_= load_dotenv(find_dotenv())

chatm = ChatGroq(
    model="llama3-70b-8192"
)

from langchain_core.messages import HumanMessage

messagestothechatbot = [
    HumanMessage(content="My Favorite color is blue."),
]

response = chatm.invoke(messagestothechatbot)

print("\n----------\n")

print("My favorite color is blue.")

print("\n----------\n")
print(response.content)

print("\n----------\n")

response = chatm.invoke([
    HumanMessage(content="What is my favorite color?")
])

print("\n----------\n")

print("What is my favorite color?")

print("\n----------\n")
print(response.content)

print("\n----------\n")

from langchain import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.memory import FileChatMessageHistory

memory = ConversationBufferMemory(
    chat_memory = FileChatMessageHistory("messages.json"),
    memory_key = "messages",
    return_messages=True
)

prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(llm=chatm,prompt=prompt,memory=memory)

response=chain.invoke("hello")

print("\n----------\n")

print("hello!")

print("\n----------\n")
print(response)

print("\n----------\n")

response = chain.invoke("my name is Julio")

print("\n----------\n")

print("my name is Julio")

print("\n----------\n")
print(response)

print("\n----------\n")

response = chain.invoke("what is my name?")

print("\n----------\n")

print("what is my name?")

print("\n----------\n")
print(response)

print("\n----------\n")