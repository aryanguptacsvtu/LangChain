from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
docs2 = loader.load()

print("👉 ", type(docs))
print("👉 ", type(docs2))

# print("\n👉 ", len(docs)) {Throws ERROR}
print("👉 ", len(docs2))

print("\n👉 ", docs2[1].page_content)
print("👉 ", docs2[1].metadata)

for document in docs:
    print(document.metadata)