import sys
from pathlib import Path

# Permite ejecutar este archivo directamente o como módulo desde RAG_TEST.
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from movies.data import movies
from openai import OpenAI
from dotenv import load_dotenv

from supabase_client import insert_movie

load_dotenv()

client = OpenAI()


sys.stdout.reconfigure(encoding="utf-8")


data = [
    {
        "id": movie["id"],
        "title": movie["title"],
        "overview": movie["overview"],
        "release_date": movie["release_date"],
    }
    for movie in movies["results"]
]

for movie in data:
    content = f"Title: {movie['title']} Overview: {movie['overview']}"

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=content,
        encoding_format="float",
    )

    embedding = response.data[0].embedding

    try:
        insert_movie(
            vector=embedding,
            content=content,
            metadata={
                "id": movie["id"],
                "title": movie["title"],
                "overview": movie["overview"],
                "release_date": movie["release_date"],
            },
        )
    except Exception as error:
        print(f"Error al insertar la película {movie['id']}: {error}")
    else:
        print(f"Película {movie['id']} insertada correctamente")
