from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = ["Delhi is the capital of India",
             "Kolkata is the capital of West Bengal",
             "Paris is the capital of France"]

query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)

print(sorted(list(enumerate(scores)), key=lambda x:x[1]))  # Ascending Order

print(sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]) # Highest Score

max_index , max_score = sorted( list(enumerate(scores)), key=lambda x:x[1] )[-1]

print(documents[max_index])  
print("Highest Similarity Score :",max_score)