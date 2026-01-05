from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="gemma2-9b-it", temperature=0.5)
# model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5)

prompt = PromptTemplate(
    template = "Generate 5 interesting facts about {topic}.",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser   # Langchain Expression Language(LCE)

result = chain.invoke({'topic': 'space'})
print(result)

chain.get_graph().print_ascii()
