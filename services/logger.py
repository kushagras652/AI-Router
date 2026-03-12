from database.db import conn

cursor = conn.cursor()


def log_query(prompt, model, complexity, latency, tokens, cost):

    cursor.execute("""
    INSERT INTO query_logs 
    (prompt, model_used, complexity_level, latency, tokens_used, cost)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (prompt, model, complexity, latency, tokens, cost))

    conn.commit()