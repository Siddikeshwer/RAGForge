import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Generator:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.model = os.getenv(
            "MODEL",
            "stealth/ox-alpha"
        )

        if not self.api_key:
            raise ValueError(
                "OPENROUTER_API_KEY is missing"
            )

    def generate(
        self,
        question: str,
        documents: list[dict]
    ) -> str:

        context_parts = []

        for i, item in enumerate(documents, 1):

            metadata = item.get("metadata", {})

            source = metadata.get(
                "source",
                "Unknown"
            )

            page = metadata.get("page")

            location = f"Page {page}" if page else "Document"

            context_parts.append(
                f"[Source {i}]\n"
                f"File: {source}\n"
                f"Location: {location}\n"
                f"Content:\n{item['document']}"
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
You are RAGForge, a document question-answering assistant.

Answer the user's question using ONLY the provided context.

Rules:
1. Do not invent information.
2. If the answer is not present, say:
   "I couldn't find the answer in the provided documents."
3. Cite claims using [Source N].
4. Only cite sources that actually support the claim.
5. Keep the answer concise.

Context:

{context}

Question:

{question}
"""

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]