from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore


embedding_model = EmbeddingModel()
vector_store = VectorStore()


documents = [
    "You can reset your password from Settings > Security.",
    "Python is a popular programming language.",
    "The company provides cloud computing services."
]

embeddings = embedding_model.embed_documents(documents)

ids = ["doc1", "doc2", "doc3"]

vector_store.add_documents(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)


query = "How can I change my password?"

query_embedding = embedding_model.embed_text(query)

results = vector_store.search(
    query_embedding=query_embedding,
    top_k=2
)


print("\nRetrieved documents:\n")

for document in results["documents"][0]:
    print("-", document)