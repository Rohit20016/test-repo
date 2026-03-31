from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{username}'")
    return cursor.fetchall()

@app.route("/user")
def user():
    username = request.args.get("username")
    return str(get_user(username))
