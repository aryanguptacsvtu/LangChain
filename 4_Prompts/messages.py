from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
model = ChatGroq(model="gemma2-9b-it", temperature=0)

messages = [ SystemMessage(content='You are a helpful assistant'),
            HumanMessage(content='Tell me about LangChain')]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)