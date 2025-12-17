from retrieval import PubMedRetriever

r = PubMedRetriever()

results = r.search(
    "hallucinations in large language models in medical research",
    k=3
)

for res in results:
    print("\nTITLE:", res["title"])
    print(res["abstract"][:300])
