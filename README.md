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


## License
Apache 2.0

<h3 align="center">Model Performance</h3>

<p align="center">
<svg width="420" height="260" viewBox="0 0 420 260">
  <!-- Axes -->
  <line x1="50" y1="20" x2="50" y2="220" stroke="#999"/>
  <line x1="50" y1="220" x2="380" y2="220" stroke="#999"/>

  <!-- Bars -->
  <rect x="90" y="90" width="60" height="130" fill="#2563EB"/>
  <rect x="180" y="60" width="60" height="160" fill="#16A34A"/>
  <rect x="270" y="40" width="60" height="180" fill="#DC2626"/>

  <!-- Labels -->
  <text x="95" y="240" font-size="12">TF-IDF</text>
  <text x="175" y="240" font-size="12">BERT</text>
  <text x="255" y="240" font-size="12">BERT + GNN</text>

  <text x="20" y="30" font-size="12">Accuracy</text>

  <!-- Values -->
  <text x="100" y="85" font-size="12">0.71</text>
  <text x="190" y="55" font-size="12">0.82</text>
  <text x="280" y="35" font-size="12">0.89</text>
</svg>
</p>


