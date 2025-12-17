from evaluator import Evaluator

answers = [
    "Large language models are used in healthcare. They never hallucinate.",
    "Several studies show hallucinations are a major concern in medical AI.",
    "LLMs can assist clinicians but may produce unsupported claims."
]

evaluator = Evaluator()
metrics = evaluator.evaluate(answers)

print("\nEVALUATION METRICS")
for k, v in metrics.items():
    print(f"{k}: {v}")
