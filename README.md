# FakeNews-GNN 🔗

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.15-red)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)

##  Overview
Detect fake news using **Graph Neural Networks (GCN / GAT)** by combining **text embeddings** (BERT) and **graph connections** between news, authors, and sources.

##  Project Structure
data/ # raw & processed datasets
models/ # GNN & text embeddings
training/ # train & evaluate scripts
utils/ # graph building & metrics
demo/ # Streamlit interactive demo


##  Usage
pip install -r requirements.txt
python training/train.py
python training/evaluate.py
streamlit run demo/streamlit_app.py


##License
Apache 2.0


