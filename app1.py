import streamlit as st
from rag_graph import ask_question

# Titre de l'application
st.set_page_config(page_title="Agentic RAG Chatbot", layout="centered")

st.title("🤖 Chatbot RAG avec LangGraph")
st.write("Pose une question sur ton document PDF")

# Zone de saisie utilisateur
question = st.text_input("💬 Ta question :")

# Bouton envoyer
if st.button("Envoyer"):
    if question:
        with st.spinner("Recherche en cours..."):
            response = ask_question(question)
        st.success("Réponse :")
        st.write(response)
    else:
        st.warning("Veuillez entrer une question.")