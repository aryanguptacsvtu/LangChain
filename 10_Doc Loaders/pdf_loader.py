from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print("👉 ",len(docs))
print("👉 ",type(docs))

print(docs[10].page_content)
print(docs[17].metadata)