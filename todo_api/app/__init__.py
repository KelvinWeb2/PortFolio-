from flask import Flask
from app.routes import app

def create_app():
    """Create and configure the app"""
    app.config['DEBUG'] = True
    return app
