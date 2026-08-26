from app.rag.bm25 import BM25Store


documents = [
    "You can reset your password from Settings > Security.",
    "Python is a popular programming language.",
    "AWS Lambda has a maximum execution timeout."
]

bm25 = BM25Store()

bm25.add_documents(documents)

query = "AWS Lambda timeout"

results = bm25.search(query, top_k=3)

print("\nBM25 Results:\n")

for result in results:
    print(f"Score: {result['score']:.4f}")
    print(result["document"])
    print()