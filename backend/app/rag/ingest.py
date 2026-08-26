from pathlib import Path

from app.rag.loader import load_document
from app.rag.chunker import chunk_text
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore
from app.rag.bm25 import BM25Store


class DocumentIngestor:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()
        self.bm25_store = BM25Store()

    def ingest(self, file_path: str):

        pages = load_document(file_path)

        all_chunks = []
        metadatas = []

        for page in pages:

            chunks = chunk_text(page["text"])

            for chunk in chunks:
                all_chunks.append(chunk)

                metadatas.append({
                    "source": page["source"],
                    "page": page["page"]
                })

        if not all_chunks:
            raise ValueError("Document contains no readable text.")

        embeddings = self.embedding_model.embed_documents(
            all_chunks
        )

        file_name = Path(file_path).stem

        ids = [
            f"{file_name}_{i}"
            for i in range(len(all_chunks))
        ]

        self.vector_store.add_documents(
            documents=all_chunks,
            embeddings=embeddings,
            ids=ids,
            metadatas=metadatas
        )

        self.bm25_store.add_documents(
            all_chunks,
            metadatas
        )

        return {
            "file": file_name,
            "chunks": len(all_chunks)
        }