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

<h3 align="center">📊 Model Accuracy Comparison</h3>

<p align="center">
<svg width="420" height="260" viewBox="0 0 420 260">

  <!-- Axes -->
  <line x1="50" y1="20" x2="50" y2="220" stroke="#aaa"/>
  <line x1="50" y1="220" x2="380" y2="220" stroke="#aaa"/>

  <!-- Bar 1 -->
  <rect x="90" y="220" width="60" height="0" fill="#2563EB">
    <animate attributeName="height" from="0" to="130" dur="1s" fill="freeze"/>
    <animate attributeName="y" from="220" to="90" dur="1s" fill="freeze"/>
  </rect>

  <!-- Bar 2 -->
  <rect x="180" y="220" width="60" height="0" fill="#16A34A">
    <animate attributeName="height" from="0" to="160" dur="1.2s" fill="freeze"/>
    <animate attributeName="y" from="220" to="60" dur="1.2s" fill="freeze"/>
  </rect>

  <!-- Bar 3 -->
  <rect x="270" y="220" width="60" height="0" fill="#DC2626">
    <animate attributeName="height" from="0" to="180" dur="1.4s" fill="freeze"/>
    <animate attributeName="y" from="220" to="40" dur="1.4s" fill="freeze"/>
  </rect>

  <!-- Labels -->
  <text x="95" y="245" font-size="12">TF-IDF</text>
  <text x="175" y="245" font-size="12">BERT</text>
  <text x="255" y="245" font-size="12">BERT + GNN</text>

  <!-- Values -->
  <text x="105" y="80" font-size="12">0.71</text>
  <text x="195" y="50" font-size="12">0.82</text>
  <text x="285" y="30" font-size="12">0.89</text>

</svg>
</p>
