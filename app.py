from flask import request

@app.route("/user")
def user():
    username = request.args.get("username")
    return get_user(username)
