import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama  # Usa Ollama invece di OpenAI

# Funzione per caricare e processare il PDF
def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(pages, embeddings, persist_directory="./chroma_db")
    return db

# Funzione per interrogare il database
def query_db(db, query):
    # llm = Ollama(model="llama2")  # Usa il modello LLaMA 2 di Ollama
    
#   llm = ChatOllama(model="llama3.2", temperature=0, max_tokens=300)
    llm = Ollama(base_url="http://ollama:11434", model="llama3.2")
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
    result = qa.run(query)
    return result

# Interfaccia Streamlit
st.title("Chatbot per PDF con Chroma, LangChain e Ollama")

uploaded_file = st.file_uploader("Carica un file PDF", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    db = process_pdf("temp.pdf")
    st.success("PDF caricato e processato con successo!")

    query = st.text_input("Fai una domanda sul documento:")
    if query:
        answer = query_db(db, query)
        st.write("Risposta:", answer)