from flask import Flask
from .views import register_blueprints

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # Configure your app (e.g., load config from .env)

    # Register your blueprints
    register_blueprints(app)

    # Initialize your memory_repo and other extensions
    # memory_repo.init_app(app)

    return app