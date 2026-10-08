from html import escape

from flask import Flask, jsonify, request

from supabase_client import insert_movie, supabase


app = Flask(__name__)

@app.route("/")
def index():
    response = supabase.table("Movies").select("*").execute()
    movies = response.data

    html = "<h1>Movies</h1><ul>"
    for movie in movies:
        html += f'<li>{escape(str(movie.get("title", "")))}</li>'
    html += "</ul>"

    return html


@app.post("/movies")
def create_movie():
    body = request.get_json(silent=True) or {}

    required_fields = ("vector", "content", "metadata")
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"error": f"Faltan campos: {', '.join(missing_fields)}"}), 400

    try:
        inserted = insert_movie(
            body["vector"],
            body["content"],
            body["metadata"],
        )
        return jsonify(inserted), 201
    except Exception as error:
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True)
