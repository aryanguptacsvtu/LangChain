from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import openai
from langchain.chains import retrieval_qa

# Load the dataset
loader = TextLoader('docs.txt')
documents = loader.load()

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Convert the text chunks into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# Create a Retriever[Fetches relevant documents]
retriever = vectorstore.as_retriever()

# Initialize the LLM
llm = openai(model="gpt-3.5-turbo",temperature=0.5)

# Create RetrievalQA chain
qa_chain = retrieval_qa(llm=llm , retriever=retriever)

# Ask a question
query = "What are key takeawys from the document?"
answer = qa_chain.run(query)

print(answer)
