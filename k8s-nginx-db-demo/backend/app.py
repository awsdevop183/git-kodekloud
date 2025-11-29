from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "/data/visits.db"


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.route("/api/status")
def status():
    pod_name = os.getenv("HOSTNAME", "unknown-pod")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # insert one row per request
    cur.execute("INSERT INTO visits DEFAULT VALUES;")
    conn.commit()

    # count total visits
    cur.execute("SELECT COUNT(*) FROM visits;")
    total_visits = cur.fetchone()[0]

    cur.close()
    conn.close()

    return jsonify({
        "pod": pod_name,
        "total_visits": total_visits
    })


@app.route("/")
def health():
    return "Backend is running\n"


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
