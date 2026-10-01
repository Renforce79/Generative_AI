from text import text
import re


def chunk_text(text, min_length=100, max_length=120, overlap=40):
    if overlap >= max_length:
        raise ValueError("overlap debe ser menor que max_length")

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        candidate = f"{current_chunk} {sentence}".strip()

        if len(candidate) > max_length and current_chunk:
            chunks.append(current_chunk)

            # Conserva los últimos caracteres para dar contexto al chunk siguiente.
            previous_context = current_chunk[-overlap:]
            current_chunk = f"{previous_context} {sentence}".strip()
        elif len(candidate) < min_length:
            current_chunk = candidate
        else:
            current_chunk = candidate

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


chunks = chunk_text(text)

for chunk in chunks:
    print("Chuuuuuuuunk:", chunk)
