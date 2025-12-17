import json
import pickle
import faiss
from sentence_transformers import SentenceTransformer

DATA_PATH = "data/raw/pubmed_sample.jsonl"
INDEX_PATH = "data/faiss.index"
META_PATH = "data/metadata.pkl"

papers = []
texts = []

with open(DATA_PATH, "r", encoding="utf-8") as f:
    for line in f:
        paper = json.loads(line)
        if "title" in paper and "abstract" in paper:
            papers.append(paper)
            texts.append(f"{paper['title']} {paper['abstract']}")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, INDEX_PATH)

with open(META_PATH, "wb") as f:
    pickle.dump(papers, f)

print(f"Indexed {len(papers)} PubMed papers")
