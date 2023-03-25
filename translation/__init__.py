from flask import Flask
from .views import register_blueprints

def create_app():
    app = Flask(__name__)

    # Register blueprints for views
    register_blueprints(app)

    return app
