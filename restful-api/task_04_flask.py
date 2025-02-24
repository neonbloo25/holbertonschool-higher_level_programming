from flask import Flask, jsonify, request
app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()

    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    users[new_user["username"]] = new_user

    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5001)
