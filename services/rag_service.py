from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

VECTOR_DB_PATH='vector_store'

embeddings=OpenAIEmbeddings()

def ingest_document(file_path):
    loader=PyPDFLoader(file_path)

    documents=loader.load()

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks=splitter.split_documents(documents)

    vector_store=FAISS.from_documents(chunks,embeddings)

    vector_store.save_local(VECTOR_DB_PATH)

    return "Document indexed successfully"


def retrieve_content(query):
    vector_store=FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs=vector_store.similarity_search(query,k=3)

    context="\n\n".join([doc.page_content for doc in docs])

    return context