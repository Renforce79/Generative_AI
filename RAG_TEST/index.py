from openai import OpenAI

client = OpenAI()

text = "Este es un documento sobre arquitectura de datos."

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

embedding = response.data[0].embedding

print(f"Dimensiones: {len(embedding)}")
print(embedding[:5])