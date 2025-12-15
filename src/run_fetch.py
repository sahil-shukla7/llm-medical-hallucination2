import json
from fetch_pubmed import fetch_pubmed

QUERY = "large language models medical hallucination"

def main():
    papers = fetch_pubmed(QUERY, retmax=50)

    with open("data/raw/pubmed_sample.jsonl", "w", encoding="utf-8") as f:
        for paper in papers:
            f.write(json.dumps(paper) + "\n")

    print(f"Saved {len(papers)} papers")

if __name__ == "__main__":
    main()
