import matplotlib.pyplot as plt

metrics = {
    "Supported": 0.33,
    "Contradicted": 0.0,
    "Hallucinated": 0.67
}

plt.bar(metrics.keys(), metrics.values())
plt.ylabel("Rate")
plt.title("Hallucination Evaluation Metrics")
plt.ylim(0, 1)
plt.savefig("assets/metrics.png")
plt.close()
