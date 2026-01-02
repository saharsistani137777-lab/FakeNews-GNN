# FakeNews-GNN 🔗

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.15-red)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

##  Project Overview

**FakeNews-GNN** is a Graph Neural Network (GNN) based system for detecting fake news using **textual content** and **network information** like authors, sources, and user interactions.

> This project explores **how deep learning models can leverage graph structures to improve fake news detection**, providing insights into node relations and embedding overlaps.

---

##  Features

- **Textual embeddings**: BERT-based embeddings for news text
- **Graph construction**: News, authors, sources, and their connections
- **GNN models**: GCN and GAT for node classification
- **Evaluation**: Accuracy, F1-Score, ROC-AUC
- **Interactive demo**: Streamlit app for real-time predictions
- **Explainable AI**: Analyze attention and embeddings for interpretability

---

##  Architecture

```mermaid
graph TD;
    Text[News Text] -->|BERT Embedding| NodeFeature[Node Features];
    NodeFeature --> GNN[Graph Neural Network (GCN / GAT)];
    GNN --> Prediction[Fake / Real];
    News -->|Author / Source| NodeFeature;

