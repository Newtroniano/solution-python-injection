from flask import jsonify, request, Blueprint
from app.Controllers.user_controller import UserController

user = Blueprint('user', __name__)

# Rota para obter todos os usuários
@user.route('/users', methods=['GET'])
def get_users():
    users = UserController.get_all_users()
    return jsonify(users=users)

# Rota para obter um usuário específico pelo ID
@user.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserController.get_user_by_id(user_id)
    if user:
        return jsonify(user=user)
    return jsonify(error="Usuário não encontrado"), 404
