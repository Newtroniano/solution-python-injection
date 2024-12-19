# controllers/user_controller.py

from app.Models.user_model import User
from app import db
import pandas as pd
from flask import jsonify

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

                # Verifica o nome da planilha para determinar qual tabela usar
                table_name = sheet_name.lower().replace(' ', '_')  # Converte para o formato de nome da tabela
                model_class = globals().get(table_name.capitalize())

                if model_class:
                    # Itera sobre os registros do DataFrame e insere no banco de dados
                    for index, row in df.iterrows():
                        new_entry = model_class(**row.to_dict())
                        db.session.add(new_entry)

                    db.session.commit()
                else:
                    return {"message": f"Table model '{table_name.capitalize()}' not found."}, 400

            return {"message": "Data inserted successfully!"}, 200

        except Exception as e:
            db.session.rollback()
            return {"message": f"An error occurred: {str(e)}"}, 500