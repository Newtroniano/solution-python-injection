from flask import Flask
from app.services import MyService

def configure_dependencies(app: Flask):
    app.config.from_object('app.config.DevelopmentConfig')
    app.service = MyService()
