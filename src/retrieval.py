import faiss
import pickle
from sentence_transformers import SentenceTransformer

class PubMedRetriever:
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.index = faiss.read_index("data/faiss.index")

        with open("data/metadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query, k=5):
        q_emb = self.model.encode([query]).astype("float32")
        _, idx = self.index.search(q_emb, k)
        return [self.metadata[i] for i in idx[0]]
