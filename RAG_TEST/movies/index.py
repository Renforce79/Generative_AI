import json
import sys
from data import movies
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


sys.stdout.reconfigure(encoding="utf-8")


data = [
    {
        "id": movie["id"],
        "title": movie["title"],
        "overview": movie["overview"],
    }
    for movie in movies["results"]
]

for movie in data:
    texto = f"Title: {movie['title']} Overview: {movie['overview']}"

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texto,
        encoding_format="float",
    )

    print(json.dumps(response.data[0].embedding, ensure_ascii=False))
