# controllers/user_controller.py

from app.Models.user_model import User
from app import db

class UserController:
    @staticmethod
    def get_all_users():
        
        return [user.to_dict() for user in User.query.all()]

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            return user.to_dict()
        return None

    @staticmethod
    def add_user(name, email):
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()

    @staticmethod
    def update_user(user_id, name, email):
        user = User.query.get(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
            return user.to_dict()
        return None

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
