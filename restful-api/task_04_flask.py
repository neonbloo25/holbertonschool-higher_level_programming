from flask import Flask, jsonify, request
"""restfulAPI week ft flask"""

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"},
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"}
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data.get('username'):
        return jsonify({"error": "Username is required"}), 400

    users[data['username']] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
