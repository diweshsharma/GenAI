# from pypdf import PyPDF
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Diwesh_CV.pdf')

result = loader.load()
print(result[0].page_content)