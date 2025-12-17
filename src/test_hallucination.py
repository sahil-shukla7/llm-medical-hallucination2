from hallucination_detector import HallucinationDetector

detector = HallucinationDetector()

llm_answer = """
Large language models are widely used in medicine.
They never hallucinate when answering medical questions.
Several studies have shown that hallucinations remain a major concern in medical AI.
"""

results = detector.analyze(llm_answer)

for r in results:
    print("\nCLAIM:", r["claim"])
    print("VERDICT:", r["verdict"])
    print("CONFIDENCE:", r["confidence"])
