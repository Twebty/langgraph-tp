
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv.ipython import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken
from langchain.tools import tool
from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv(override=True)

loader = PyPDFLoader("cv.pdf")
tokennizer = tiktoken.encoding_for_model('gpt-4o-mini')

splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    encoding_name= tokennizer.name,
    chunk_size=300,
    chunk_overlap=20
)
chunks = loader.load_and_split(splitter)
embedding_model=OpenAIEmbeddings()
vector_stor = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="cv_data_collection"
)
retriever = vector_stor.as_retriever(kwargs={"fetch_k": 10})
@tool
def retriever_tool(query : str) ->str:
    """
    permet de chercher des info sur des candidat:
    nom,prenom ,diplomeexperience
    competence
    """
    relevent_chunks = retriever.invoke(query)
    context_list = [d.page_content for d in relevent_chunks]
    context = ". ".join(context_list)
    return context
@tool
def get_company_infos(company_name :str):
    """consulter des info sur entreprise donne
    """
    return {
        "company_name": company_name,
        "location": "Paris, France",
        "industry": "Technology",
        "size": "500-1000 employees",
        "founded": "2010",
        
    }
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 4
agent = initialize_agent(
    tools=[retriever_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)