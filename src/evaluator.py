from hallucination_detector import HallucinationDetector

class Evaluator:
    def __init__(self):
        self.detector = HallucinationDetector()

    def evaluate(self, llm_answers):
        total = 0
        supported = 0
        contradicted = 0
        unsupported = 0

        for answer in llm_answers:
            results = self.detector.analyze(answer)
            for r in results:
                total += 1
                if r["verdict"] == "supported":
                    supported += 1
                elif r["verdict"] == "contradicted":
                    contradicted += 1
                else:
                    unsupported += 1

        return {
            "total_claims": total,
            "support_rate": round(supported / total, 3),
            "contradiction_rate": round(contradicted / total, 3),
            "hallucination_rate": round((unsupported + contradicted) / total, 3),
        }
