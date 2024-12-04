import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

def scrape_website(url):
    data = []
    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            data.append(soup.get_text(strip=True))
            next_page = soup.select_one("a.next-page")
            url = urljoin(url, next_page["href"]) if next_page else None
        except Exception as e:
            break
    return " ".join(data)

def index_data(data):
    if not data:
        raise ValueError("No data to index!")
    embeddings = OllamaEmbeddings(model="llama3.2")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(data)
    vectorstore = FAISS.from_texts(chunks, embeddings)
    return vectorstore

def create_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    llm = OllamaLLM(model="llama3.2")
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return rag_chain
