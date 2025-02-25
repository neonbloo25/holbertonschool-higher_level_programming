from flask import Flask, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username

@app.route('/protected')
@auth.login_required
def protected():
    return jsonify({"message": "This is a protected route", "user": auth.current_user()})

@app.route('/admin')
@auth.login_required
def admin():
    if users[auth.current_user()]["role"] != "admin":
        return jsonify({"message": "You must be an admin to access this route"}), 403
    return jsonify({"message": "Welcome, admin!"})

if __name__ == '__main__':
    app.run(debug=True)
