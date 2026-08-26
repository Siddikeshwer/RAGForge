import chromadb


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="ragforge"
        )

    def add_documents(
        self,
        documents: list[str],
        embeddings: list[list[float]],
        ids: list[str],
        metadatas: list[dict]
    ):
        self.collection.upsert(
            documents=documents,
            embeddings=embeddings,
            ids=ids,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 5
    ):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )