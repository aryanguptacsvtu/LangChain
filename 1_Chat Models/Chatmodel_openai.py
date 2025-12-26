from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Creating ChatOpenAI object
model = ChatOpenAI(model='gpt-4',temperature=0.5,max_completion_tokens=10)

result = model.invoke("What is the capital of India")

print(result)  # To get the entire response object
print(result.content)  # To get the content of the response