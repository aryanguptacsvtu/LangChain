from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

# print(docs)
print("👉 ", len(docs))
print("👉 ", type(docs))
print("👉 ", type(docs[10]))

print(docs[1])