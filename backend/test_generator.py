from app.rag.generator import Generator


generator = Generator()

documents = [
    "AWS Lambda has a maximum execution timeout."
]

question = "What is the AWS Lambda timeout?"

answer = generator.generate(
    question=question,
    documents=documents
)

print("\n=== OX ALPHA ===\n")
print(answer)