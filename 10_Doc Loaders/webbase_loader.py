from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="gemma2-9b-it", temperature=0)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser
print("👉 ", type(docs))
print("👉 ", len(docs))
print("👉 ", docs[0].metadata,"\n")

# print(chain.invoke({'question':'What is the topic that we are talking about?', 'text':docs[0].page_content}))