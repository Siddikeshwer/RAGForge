from app.rag.embeddings import EmbeddingModel
import numpy as np


embedding_model = EmbeddingModel()

texts = [
    "How do I reset my password?",
    "I forgot my password and want to change it.",
    "What is the capital of France?"
]

vectors = embedding_model.embed_documents(texts)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


print("Password vs Password:")
print(cosine_similarity(vectors[0], vectors[1]))

print("\nPassword vs France:")
print(cosine_similarity(vectors[0], vectors[2]))