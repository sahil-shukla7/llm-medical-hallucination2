from transformers import pipeline

class ClaimVerifier:
    def __init__(self):
        self.nli = pipeline(
            "text-classification",
            model="facebook/bart-large-mnli"
        )

    def verify(self, claim, evidence):
        text = f"{evidence} </s></s> {claim}"
        result = self.nli(text, truncation=True)[0]

        label = result["label"].lower()
        score = result["score"]

        if label == "entailment":
            return "supported", score
        elif label == "contradiction":
            return "contradicted", score
        else:
            return "unsupported", score
