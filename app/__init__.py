# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    
    from .routes.user import main as user_routes_blueprint
    from .routes.upload import upload_routes as upload_routes_blueprint
    app.register_blueprint(user_routes_blueprint, url_prefix='/api')
    app.register_blueprint(upload_routes_blueprint, url_prefix='/api')

    
    return app
