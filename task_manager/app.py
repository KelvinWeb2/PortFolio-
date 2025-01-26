
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# In-memory database for users (for simplicity)
users = []

# Register route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Check if user already exists
    for user in users:
        if user['username'] == username:
            return jsonify({"error": "User already exists"}), 400

    # Hash the password and save the user
    hashed_password = generate_password_hash(password)
    users.append({"username": username, "password": hashed_password})

    return jsonify({"message": "User registered successfully"}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Find the user
    for user in users:
        if user['username'] == username:
            # Check password
            if check_password_hash(user['password'], password):
                return jsonify({"message": "Login successful"}), 200
            else:
                return jsonify({"error": "Invalid password"}), 401

    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
