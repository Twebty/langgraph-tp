from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Charger PDF
loader = PyPDFLoader("documents/cours.pdf")
documents = loader.load()

# Découpage
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# Embeddings
embeddings = OpenAIEmbeddings()

# Base vectorielle
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="chroma_db"
)

retriever = db.as_retriever()

# Modèle IA
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Chaîne RAG
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

def ask_question(question):
    return qa.run(question)