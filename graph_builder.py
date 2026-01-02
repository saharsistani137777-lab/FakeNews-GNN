import torch
import pandas as pd

def build_graph(df, embeddings_dict):
    nodes = {}
    node_id = 0
    edge_index = []

    for _, row in df.iterrows():
        for key in [row['news_id'], row['author'], row['source']]:
            if key not in nodes:
                nodes[key] = node_id
                node_id += 1

    for _, row in df.iterrows():
        n_id = nodes[row['news_id']]
        a_id = nodes[row['author']]
        s_id = nodes[row['source']]
        edge_index += [[n_id, a_id],[a_id, n_id],[n_id, s_id],[s_id, n_id]]
    
    edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()

    x = torch.zeros((len(nodes), 768))  
    for key, idx in nodes.items():
        x[idx] = embeddings_dict.get(key, torch.zeros(768))
    
    return x, edge_index, nodes
