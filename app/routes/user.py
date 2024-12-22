from flask import Blueprint, jsonify
from app.Controllers.user_controller import UserController

main = Blueprint('main', __name__)

@main.route('/users', methods=['GET'])
def get_users():
    users = UserController.get_all_users()
    return jsonify(users=users)

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserController.get_user_by_id(user_id)
    if user:
        return jsonify(user=user)
    return jsonify(error="Usuário não encontrado"), 404
