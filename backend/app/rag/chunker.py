import re


def chunk_text(
    text: str,
    chunk_size: int = 120,
    chunk_overlap: int = 20
) -> list[str]:

    # Split on blank lines
    sections = re.split(r"\n\s*\n", text.strip())

    chunks = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        words = section.split()

        start = 0

        while start < len(words):
            end = start + chunk_size

            chunk = " ".join(words[start:end])

            if chunk.strip():
                chunks.append(chunk)

            start += chunk_size - chunk_overlap

    return chunks