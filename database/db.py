import sqlite3

conn = sqlite3.connect("router_logs.db", check_same_thread=False)

cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS query_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt TEXT,
        model_used TEXT,
        complexity_level INTEGER,
        latency REAL,
        tokens_used INTEGER,
        cost REAL
    )
    """)

    conn.commit()

init_db()