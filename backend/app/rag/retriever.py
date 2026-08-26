from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore
from app.rag.bm25 import BM25Store


class HybridRetriever:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()
        self.bm25_store = BM25Store()

    def search(self, query: str, top_k: int = 5):
        query_embedding = self.embedding_model.embed_text(query)

        vector_results = self.vector_store.search(
            query_embedding,
            top_k
        )

        bm25_results = self.bm25_store.search(
            query,
            top_k
        )

        return self._rrf_merge(
            vector_results,
            bm25_results,
            top_k
        )

    def _rrf_merge(
        self,
        vector_results,
        bm25_results,
        top_k
    ):
        scores = {}
        documents = {}
        metadatas = {}

        # Vector results
        vector_docs = vector_results["documents"][0]
        vector_metadatas = vector_results["metadatas"][0]

        for rank, document in enumerate(vector_docs):

            metadata = vector_metadatas[rank] or {}

            scores[document] = scores.get(document, 0) + (
                1 / (60 + rank + 1)
            )

            documents[document] = document

            metadatas[document] = {
                "source": metadata.get(
                    "source",
                    "Unknown"
                ),
                "page": metadata.get(
                    "page",
                    None
                )
            }

        # BM25 results
        for rank, result in enumerate(bm25_results):

            document = result["document"]

            metadata = result.get("metadata", {})

            scores[document] = scores.get(document, 0) + (
                1 / (60 + rank + 1)
            )

            documents[document] = document

            metadatas[document] = {
                "source": metadata.get(
                    "source",
                    "Unknown"
                ),
                "page": metadata.get(
                    "page",
                    None
                )
            }

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            {
                "document": document,
                "metadata": metadatas[document],
                "score": score
            }
            for document, score in ranked[:top_k]
        ]