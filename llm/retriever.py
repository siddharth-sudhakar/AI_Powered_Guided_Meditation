import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# Load the dataset
df = pd.read_csv("C:/Users/Siddharth/OneDrive/Desktop/meditation-backend/data/RAG_Dataset.csv")

# Filter Science/Advice entries
advice_texts = df["Science/Advice"].dropna().tolist()

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Embed all advice entries
advice_embeddings = model.encode(advice_texts, show_progress_bar=True)

# Build FAISS index
embedding_dim = advice_embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dim)
index.add(np.array(advice_embeddings))

# Save original texts in memory for lookup
id_to_advice = {i: txt for i, txt in enumerate(advice_texts)}

# Retrieval function
def retrieve_relevant_advice(query: str, top_k: int = 3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [id_to_advice[i] for i in indices[0]]