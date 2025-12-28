from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India"

vector = embedding.embed_query(text)  # Embed a single query
print(str(vector))


# documents = ["Delhi is the capital of India",
#              "Kolkata is the capital of West Bengal",
#              "Paris is the capital of France"]

# vector = embedding.embed_documents(documents)  # Embed a list of documents
# print(str(result))