from app.rag.rag_pipeline import RAGPipeline


documents = [
    """
    AWS Lambda is a serverless computing service.
    Each Lambda function has a maximum execution timeout
    of 15 minutes.
    """,

    """
    Python is a high-level programming language widely used
    for web development, automation, and machine learning.
    """,

    """
    ChromaDB is a vector database designed for AI applications
    and semantic search.
    """,

    """
    BM25 is a keyword-based information retrieval algorithm.
    """,

    """
    RAG stands for Retrieval-Augmented Generation.
    It retrieves relevant information before asking an LLM
    to generate an answer.
    """
]


rag = RAGPipeline(documents)

question = "What is the maximum AWS Lambda execution timeout?"

result = rag.ask(question)

print("\n==============================")
print("ANSWER")
print("==============================\n")

print(result["answer"])

print("\n==============================")
print("SOURCES")
print("==============================\n")

for i, source in enumerate(result["sources"], 1):
    print(f"{i}. Score: {source['score']:.4f}")
    print(source["document"].strip())
    print()