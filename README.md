
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


graph TD;
    Text[News Text] -->|BERT Embedding| NodeFeature[Node Features];
    NodeFeature --> GNN[Graph Neural Network (GCN / GAT)];
    GNN --> Prediction[Fake / Real];
    News -->|Author / Source| NodeFeature;


Mermaid diagram for graph structure visualization. Shows how news text and graph info flow into GNN for predictions.


 Tech Stack
| Technology                  | Purpose                        |
| --------------------------- | ------------------------------ |
| Python 3.11                 | Programming                    |
| PyTorch & PyTorch Geometric | GNN & DL models                |
| HuggingFace Transformers    | Text embeddings (BERT)         |
| NetworkX                    | Graph analysis & visualization |
| Streamlit                   | Interactive demo               |
| Scikit-learn                | Metrics & evaluation           |


 Example Visualization
graph LR;
  FakeNews1 --> Author1;
  FakeNews1 --> Source1;
  FakeNews2 --> Author2;
  FakeNews2 --> Source1;
  Author1 --> Author2;


Shows connections between news, authors, and sources in a mini graph example.

 Usage

Install dependencies:

pip install -r requirements.txt


Prepare dataset:

Place raw CSV in data/raw/fakenews.csv

Columns: news_id,text,source,author,timestamp,label

Process embeddings and build graph:

from utils.graph_builder import build_graph
from models.text_embedding import TextEmbedder



Train model:

python training/train.py


Evaluate:

python training/evaluate.py


Run Streamlit demo:

streamlit run demo/streamlit_app.py

 Metrics

Accuracy

F1-Score

ROC-AUC

Confusion Matrix for detailed analysis

 Future Work

Temporal Graphs: track news propagation over time

Heterogeneous Graphs: include users, hashtags, comments

Explainable GNN: visualize attention weights for interpretability

Edge Attention: improve model by weighting connections

 License

This project is licensed under Apache 2.0 License - see the LICENSE
 file for details.

 Note

This project is research and learning-oriented. No real users are targeted, and ethical guidelines are followed.
