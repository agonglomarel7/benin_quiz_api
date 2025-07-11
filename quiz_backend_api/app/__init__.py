from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

# Initialisation des extensions
db = SQLAlchemy()
cors = CORS()

def create_app(config_name='default'):
    """Factory pour créer l'application Flask"""
    
    app = Flask(__name__)
    
    # Chargement de la configuration
    app.config.from_object(config[config_name])
    
    # Initialisation des extensions avec l'app
    db.init_app(app)
    cors.init_app(app)
    
    # Enregistrement des blueprints (routes)
    from app.views.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    # Création des tables de base de données
    with app.app_context():
        db.create_all()
    
    return app