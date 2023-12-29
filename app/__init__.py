# app/__init__.py

from flask import Flask
from config import DevelopmentConfig, TestingConfig, ProductionConfig
import os


def create_app():
    app = Flask(__name__)

    # Load configuration based on the FLASK_ENV environment variable
    if os.getenv("FLASK_ENV") == "production":
        app.config.from_object(ProductionConfig)
    elif os.getenv("FLASK_ENV") == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Register blueprints, initialize extensions, etc.
    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)  # , url_prefix='/')

    return app
