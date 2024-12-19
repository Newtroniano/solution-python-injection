from flask import Flask
from .routes.user import user as routes_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_blueprint, url_prefix='/api')
    return app
