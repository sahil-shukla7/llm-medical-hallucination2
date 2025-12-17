from claim_extractor import extract_claims
from retrieval import PubMedRetriever
from claim_verifier import ClaimVerifier

class HallucinationDetector:
    def __init__(self, top_k=3):
        self.retriever = PubMedRetriever()
        self.verifier = ClaimVerifier()
        self.top_k = top_k

    def analyze(self, llm_answer):
        claims = extract_claims(llm_answer)
        results = []

        for claim in claims:
            evidence_docs = self.retriever.search(claim, k=self.top_k)

            best_label = "unsupported"
            best_score = 0.0

            for doc in evidence_docs:
                label, score = self.verifier.verify(
                    claim,
                    doc["abstract"]
                )
                if score > best_score:
                    best_label = label
                    best_score = score

            results.append({
                "claim": claim,
                "verdict": best_label,
                "confidence": round(best_score, 3)
            })

        return results
