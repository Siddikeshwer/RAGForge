from sentence_transformers import CrossEncoder


class Reranker:
    def __init__(self):
        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query: str,
        documents: list[dict],
        top_k: int = 3
    ):
        pairs = [
            [query, item["document"]]
            for item in documents
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            {
                "document": item["document"],
                "metadata": item["metadata"],
                "score": float(score)
            }
            for item, score in ranked[:top_k]
        ]