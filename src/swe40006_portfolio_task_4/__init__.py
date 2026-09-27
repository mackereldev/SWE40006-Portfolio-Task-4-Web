import os
import psycopg
from flask import Flask, jsonify, request, render_template, redirect, url_for

conn = psycopg.connect(
    f"host=mackereldevswe40006-portfolio-task-4-web-db-1 dbname={os.environ['POSTGRES_DB']} user={os.environ['POSTGRES_USER']} password={os.environ['POSTGRES_PASSWORD']}"
)
app = Flask(__name__)

with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id serial PRIMARY KEY,
            author text,
            body text,
            created timestamp default current_timestamp
        )
        """)
    conn.commit()


@app.route("/")
def index():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM entries ORDER BY created DESC")
        keys = tuple([desc.name for desc in cur.description or []])
        entriesRaw = cur.fetchall()
        entries = list(map(lambda e: dict(zip(keys, e)), entriesRaw))

    return render_template("guest_book.html", entries=entries)


@app.post("/entry")
def create_entry():
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO entries (author, body) VALUES (%s, %s)",
            (request.form.get("author"), request.form.get("body")),
        )
        conn.commit()

    return redirect(url_for("index"))
