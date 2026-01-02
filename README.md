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

<!-- Architecture Diagram -->
<div align="center">

<h3>🧠 Model Architecture Overview</h3>

<div style="
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  font-family: Arial, sans-serif;
  margin-top: 20px;
">

  <!-- Input -->
  <div style="
    border: 2px solid #4F46E5;
    border-radius: 12px;
    padding: 14px 18px;
    min-width: 160px;
    text-align: center;
  ">
    <b>📰 News Text</b><br/>
    Author<br/>
    Source
  </div>

  <!-- Arrow -->
  <div style="font-size: 24px;">➡️</div>

  <!-- Embedding -->
  <div style="
    border: 2px solid #16A34A;
    border-radius: 12px;
    padding: 14px 18px;
    min-width: 180px;
    text-align: center;
  ">
    <b>🔤 Text Embedding</b><br/>
    BERT Encoder
  </div>

  <!-- Arrow -->
  <div style="font-size: 24px;">➡️</div>

  <!-- Graph -->
  <div style="
    border: 2px solid #EA580C;
    border-radius: 12px;
    padding: 14px 18px;
    min-width: 200px;
    text-align: center;
  ">
    <b>🔗 Graph Construction</b><br/>
    News ↔ Author<br/>
    News ↔ Source
  </div>

  <!-- Arrow -->
  <div style="font-size: 24px;">➡️</div>

  <!-- GNN -->
  <div style="
    border: 2px solid #DC2626;
    border-radius: 12px;
    padding: 14px 18px;
    min-width: 180px;
    text-align: center;
  ">
    <b> GNN Model</b><br/>
    GCN / GAT
  </div>

  <!-- Arrow -->
  <div style="font-size: 24px;">➡️</div>

  <!-- Output -->
  <div style="
    border: 2px solid #0F172A;
    border-radius: 12px;
    padding: 14px 18px;
    min-width: 140px;
    text-align: center;
  ">
    <b> Prediction</b><br/>
    Real / Fake
  </div>

</div>

</div>

