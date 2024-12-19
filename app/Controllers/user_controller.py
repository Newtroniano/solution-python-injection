# controllers/user_controller.py

from app.Models.user_model import User
from app import db
import pandas as pd


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

    def insert_data_from_excel(file_path):
        try:
            xls = pd.ExcelFile(file_path, engine='openpyxl')
            sheet_names = xls.sheet_names

            for sheet_name in sheet_names:
                df = xls.parse(sheet_name)

                for index, row in df.iterrows():
                    new_user = User(
                        username=row['username'],  
                        email=row['email'] , 
                        password=row['password'] 
                    )

                    db.session.add(new_user)

            db.session.commit()

            return {"message": "Data inserted successfully!"}, 200

        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500