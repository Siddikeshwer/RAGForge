from app.rag.retriever import HybridRetriever
from app.rag.reranker import Reranker
from app.rag.generator import Generator


class RAGPipeline:
    def __init__(self):
        self.retriever = HybridRetriever()
        self.reranker = Reranker()
        self.generator = Generator()

    def ask(
        self,
        question: str,
        top_k: int = 5,
        final_k: int = 3
    ):

        candidates = self.retriever.search(
            query=question,
            top_k=top_k
        )

        reranked = self.reranker.rerank(
            query=question,
            documents=candidates,
            top_k=final_k
        )

        answer = self.generator.generate(
            question=question,
            documents=reranked
        )

        return {
            "answer": answer,
            "sources": reranked
        }