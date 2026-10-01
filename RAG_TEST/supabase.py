from html import escape

from flask import Flask
from supabase import Client, create_client

from constants import SUPABASE_KEY, SUPABASE_URL


app = Flask(__name__)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route("/")
def index():
    response = supabase.table("todos").select("*").execute()
    todos = response.data

    html = "<h1>Todos</h1><ul>"
    for todo in todos:
        html += f'<li>{escape(str(todo.get("name", "")))}</li>'
    html += "</ul>"

    return html


if __name__ == "__main__":
    app.run(debug=True)
