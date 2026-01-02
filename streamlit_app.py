import streamlit as st
from text_embedding import TextEmbedder
st.title("Fake News Detection with GNN")
text_input = st.text_area("Paste news text here:")
if st.button("Predict"):
    embedder = TextEmbedder()
    emb = embedder.get_embedding(text_input)
    st.write("Prediction: Real / Fake")
