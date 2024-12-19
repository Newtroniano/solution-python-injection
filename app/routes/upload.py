from flask import Blueprint, request, jsonify
import os
import pandas as pd
from app.Controllers.user_controller import UserController
from werkzeug.utils import secure_filename

upload_routes = Blueprint('upload_routes', __name__)

UPLOAD_FOLDER = 'uploads'  
ALLOWED_EXTENSIONS = {'xlsx'}  

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Verifica se o arquivo tem uma extensão permitida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_routes.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part."}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file."}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        response = UserController.insert_data_from_excel(file_path)

        return jsonify(response)

    else:
        return jsonify({"message": "File extension not allowed."}), 400
