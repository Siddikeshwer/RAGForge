from app.rag.reranker import Reranker


query = "What is the AWS Lambda timeout?"

documents = [
    "Python is a popular programming language.",
    "AWS Lambda has a maximum execution timeout.",
    "Cloud computing provides scalable computing resources.",
    "You can reset your password from Settings > Security.",
    "Machine learning allows computers to learn from data."
]

reranker = Reranker()

results = reranker.rerank(
    query=query,
    documents=documents,
    top_k=3
)

print("\n=== RERANKED RESULTS ===\n")

for i, result in enumerate(results, 1):
    print(f"{i}. Score: {result['score']:.4f}")
    print(f"   {result['document']}\n")