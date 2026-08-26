from app.rag.retriever import HybridRetriever


documents = [
    "You can reset your password from Settings > Security.",
    "Python is a popular programming language.",
    "AWS Lambda has a maximum execution timeout.",
    "Machine learning allows computers to learn from data.",
    "Cloud computing provides scalable computing resources."
]

retriever = HybridRetriever(documents)

query = "What is the AWS Lambda timeout?"

results = retriever.search(query, top_k=5)

print("\n=== HYBRID RESULTS ===\n")

for i, result in enumerate(results, 1):
    print(f"{i}. Score: {result['score']:.4f}")
    print(f"   {result['document']}\n")