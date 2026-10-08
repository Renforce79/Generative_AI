from supabase import Client, create_client

from constants import SUPABASE_KEY, SUPABASE_URL


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_movie(vector, content, metadata):
    """Guarda un embedding y sus metadatos en la tabla movies."""
    response = (
        supabase.table("Movies")
        .insert({
            "vector": vector,
            "content": content,
            "metadata": metadata,
        })
        .execute()
    )

    return response.data
