from app.rag.rag_pipeline import RAGPipeline


rag = RAGPipeline()

questions = [
    "What is the maximum AWS Lambda timeout?",
    "What programming language does AWS Lambda support?",
    "What does RAG stand for?"
]

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("=" * 60)

    result = rag.ask(question)

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")

    for i, source in enumerate(result["sources"], 1):

        metadata = source["metadata"]

        print(f"\n[Source {i}]")
        print(f"File: {metadata.get('source', 'Unknown')}")
        print(f"Page: {metadata.get('page', 'N/A')}")
        print(f"Reranker score: {source['score']:.4f}")
        print(f"Text: {source['document']}")