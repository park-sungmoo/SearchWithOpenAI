# Bring in streamlit for UI/app interface
import streamlit as st
from common.funs import addtostorepdf, addtostoretxt, getfromstore, getfromacs, add_docs_to_kusto
from st_pages import add_indentation
import  os

st.title(":pencil: Index content and metadata into ChromaDB Store")
st.write("The documents in 'sou' folder will be indexed into both Chroma and FAISS.")
add_indentation()

def start_capture():
    #load documents into store
    store2 = addtostorepdf(folder_name="sou",collection_name="sou_coll",persist_directory="db/")
    store2 = addtostoretxt(folder_name="sou",collection_name="sou_coll",persist_directory="db/")
    store2 = getfromacs()
    #get document store
    store = getfromstore(collection_name="sou_coll")
    st.write(store.get(["metadatas"]))

def start_embed_to_kusto():
    add_docs_to_kusto()

if st.button("💡 Index documents in folder to ChromaDB"):
    st.write(start_capture())

if st.button("💡 Index documents in Azure Cognitive Services to Kusto"):
    st.write(start_embed_to_kusto())