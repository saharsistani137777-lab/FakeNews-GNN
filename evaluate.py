import torch
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

def evaluate(model, data, mask):
    model.eval()
    with torch.no_grad():
        logits = model(data.x, data.edge_index)[mask]
        preds = torch.argmax(logits, dim=1).cpu().numpy()
        labels = data.y[mask].cpu().numpy()
        acc = accuracy_score(labels, preds)
        f1 = f1_score(labels, preds)
        roc = roc_auc_score(labels, preds)
    return acc, f1, roc
