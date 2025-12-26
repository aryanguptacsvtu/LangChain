from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv  

load_dotenv()  # take environment variables from .env.

model = ChatAnthropic(model="claude-3.5-sonnet", max_retries=3)

result = model.invoke("What is the capital of France?")

print(result.content)
