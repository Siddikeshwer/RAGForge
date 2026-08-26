from app.rag.retriever import HybridRetriever


retriever = HybridRetriever()

question = "What is the maximum AWS Lambda timeout?"

results = retriever.search(
    question,
    top_k=3
)

print("\n=== RETRIEVAL RESULTS ===\n")

for i, result in enumerate(results, 1):
    print(f"{i}. Score: {result['score']:.4f}")
    print(f"Source: {result['metadata']['source']}")
    print(f"Page: {result['metadata']['page']}")
    print(f"Text: {result['document']}")
    print()