import json
from pathlib import Path

from rank_bm25 import BM25Okapi


class BM25Store:
    def __init__(self, path="./bm25_index.json"):
        self.path = Path(path)

        self.documents = []
        self.metadatas = []
        self.bm25 = None

        self._load()

    def add_documents(
        self,
        documents: list[str],
        metadatas: list[dict]
    ):
        self.documents.extend(documents)
        self.metadatas.extend(metadatas)

        self._build_index()
        self._save()

    def _build_index(self):
        tokenized_documents = [
            document.lower().split()
            for document in self.documents
        ]

        if tokenized_documents:
            self.bm25 = BM25Okapi(tokenized_documents)

    def _save(self):
        data = {
            "documents": self.documents,
            "metadatas": self.metadatas
        }

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def _load(self):
        if self.path.exists():
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.documents = data.get("documents", [])
            self.metadatas = data.get("metadatas", [])

            self._build_index()

    def search(self, query: str, top_k: int = 5):
        if not self.bm25:
            return []

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        return [
            {
                "document": self.documents[i],
                "metadata": {
                    "source": self.metadatas[i].get(
                        "source",
                        "Unknown"
                    ),
                    "page": self.metadatas[i].get(
                        "page",
                        None
                    )
                },
                "score": float(scores[i])
            }
            for i in ranked_indices
        ]