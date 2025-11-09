from langchain_community.document_loaders import WebBaseLoader

url = "https://en.wikipedia.org/wiki/Static_web_page"
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content[:1500]) # Printing first 1500 chars
