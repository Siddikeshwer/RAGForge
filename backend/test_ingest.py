from app.rag.ingest import DocumentIngestor


ingestor = DocumentIngestor()

result = ingestor.ingest(
    "sample.txt"
)

print("\n=== INGESTION COMPLETE ===")
print(f"File: {result['file']}")
print(f"Chunks: {result['chunks']}")