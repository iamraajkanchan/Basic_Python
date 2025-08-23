from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # For now: hardcoded user check
    if username == "raaj" and password == "your_password":
        # Store username as identity inside JWT
        token = create_access_token(identity=username)
        return jsonify(access_token=token)

    return jsonify(error="Invalid credentials"), 401
