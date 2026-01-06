from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

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

# Manually Retrieve relevant Documents
query = "What are key takeawys from the document?"
relevant_docs = retriever.get_relevant_documents(query)

# Combine Retrieved Text into a Single Prompt
retrieved_text = "\n".join([doc.page_content for doc in relevant_docs])

# Initialize the LLM
llm = OpenAI(model="gpt-3.5-turbo",temperature=0.5)

# Manually pass retrieved text to the LLM
prompt = f"Given the following text: {retrieved_text}\n\nPlease answer the question: {query}"
answer = llm.predict(prompt)

# Print the answer
print("Answer : ", answer)