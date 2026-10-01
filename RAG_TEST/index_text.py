from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

texto = "Renato es Data Engineer y trabaja con Python, PostgreSQL y tecnologías cloud."

response = client.embeddings.create(
    input=texto,
    model="text-embedding-3-small"
)

embedding = response.data[0].embedding

print("Embedding generado correctamente")
print("Dimensiones:", len(embedding))
print("Primeros 10 valores:", embedding[:10])