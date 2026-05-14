import streamlit as st
st.title('VectorDB Project')
import os
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader

os.environ['OPENAI_API_KEY'] = 'sk-'
llm = OpenAI(temperature = 0.6)

def formatt(response):
    st.success(response['result'])
    st.success('Sources:')
    for source in response["source_documents"]:
        st.success(source.metadata['source'])

useri = st.text_input("Enter file path")
user_input = st.text_input("Enter your query")
if(st.button('Submit')):
    loader = DirectoryLoader(useri, glob = "./*.txt", loader_cls= TextLoader)
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
    text = text_splitter.split_documents(document)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    persist_directory = 'db5'
    vectordb = Chroma.from_documents(documents=text,
                                 embedding=embeddings,
                                 persist_directory=persist_directory)

    vectordb.persist()
    vectordb = Chroma(persist_directory=persist_directory,
                  embedding_function=embeddings)
    
    retriever = vectordb.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                  chain_type="stuff",
                                  retriever=retriever,
                                  return_source_documents=True)


    response = qa_chain(user_input)
    formatt(response)








