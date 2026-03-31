import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Intentionally insecure (CodeQL will flag this)
    cursor.execute(
        f"SELECT * FROM users WHERE name = '{username}'"
    )

    return cursor.fetchall()