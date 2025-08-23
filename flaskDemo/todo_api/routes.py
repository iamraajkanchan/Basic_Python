from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db, ToDo

todo_bp = Blueprint("todo", __name__)

@todo_bp.route("/todos", methods=["GET"])
@jwt_required()
def get_todos():
    username = get_jwt_identity()
    todos = ToDo.query.filter_by(user_id=username).all()
    return jsonify([
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "created_at": todo.created_at.strftime("%Y-%m-%d %H:%M:%S")
        } for todo in todos
    ])

@todo_bp.route("/todos", methods=["POST"])
@jwt_required()
def create_todo():
    username = get_jwt_identity()
    data = request.get_json()
    todo = ToDo(user_id=username, title=data["title"], description=data.get("description", ""))
    db.session.add(todo)
    db.session.commit()
    return jsonify({"message": "ToDo created"}), 201

@todo_bp.route("/todos/<int:id>", methods=["PUT"])
@jwt_required()
def update_todo(id):
    username = get_jwt_identity()
    todo = ToDo.query.filter_by(id=id, user_id=username).first()
    if not todo:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    todo.title = data.get("title", todo.title)
    todo.description = data.get("description", todo.description)
    db.session.commit()
    return jsonify({"message": "ToDo updated"})

@todo_bp.route("/todos/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_todo(id):
    username = get_jwt_identity()
    todo = ToDo.query.filter_by(id=id, user_id=username).first()
    if not todo:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "ToDo deleted"})
