from flask import Flask
from redis import Redis
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)
r = Redis(host='redis-server', port=6379, db=0)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "db"),
        database=os.environ.get("POSTGRES_DB", "mydb"),
        user=os.environ.get("POSTGRES_USER", "user"),
        password=os.environ.get("POSTGRES_PASSWORD", "password")
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            visited_at TIMESTAMP NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/info")
def info():
    C = r.incr("info_count")
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Insert a new visit with current timestamp
        #now = datetime.now()
        cur.execute("INSERT INTO visits (visited_at) VALUES (%s);", (C,))
        conn.commit()

        # Read number of visits and last visit timestamp
        cur.execute("SELECT COUNT(*), MAX(visited_at) FROM visits;")
        count, last_visit = cur.fetchone()

        cur.close()
        conn.close()

        return (
            f"<h1>Hello from Flask + PostgreSQL</h1>"
            f"<p>Total visits: {count}</p>"
            f"<p>Last visit: {last_visit}</p>"
        )

    except Exception as e:
        return f"<p>Error: {e}</p>"

@app.route("/del")
def del_info():
    C = r.decr("info_count")
    return f"Декрементуємо значення до {C}"

if __name__ == "__main__":
    # Runs the app on localhost at port 5000 in debug mode
    app.run(host="0.0.0.0", port=5000, debug=True)