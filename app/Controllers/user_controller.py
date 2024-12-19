from flask import jsonify, request
from app.Models.user_model import User

class UserController:
    users = [
        User(1, "Alice", "alice@example.com"),
        User(2, "Bob", "bob@example.com"),
    ]

    @staticmethod
    def get_all_users():
        return [user.to_dict() for user in UserController.users]

    @staticmethod
    def get_user_by_id(user_id):
        user = next((user for user in UserController.users if user.id == user_id), None)
        if user:
            return user.to_dict()
        return None

    @staticmethod
    def add_user(name, email):
        new_id = max(user.id for user in UserController.users) + 1 if UserController.users else 1
        new_user = User(new_id, name, email)
        UserController.users.append(new_user)
        return new_user.to_dict()

    @staticmethod
    def update_user(user_id, name, email):
        user = next((user for user in UserController.users if user.id == user_id), None)
        if user:
            user.name = name
            user.email = email
            return user.to_dict()
        return None

    @staticmethod
    def delete_user(user_id):
        user = next((user for user in UserController.users if user.id == user_id), None)
        if user:
            UserController.users.remove(user)
            return True
        return False
