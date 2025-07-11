import os
from datetime import timedelta

class Config:
    """Configuration de base pour l'application Flask"""
    
    # Clé secrète pour sécuriser les sessions (CHANGEZ-LA EN PRODUCTION!)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre-cle-secrete-tres-longue-et-complexe'
    
    # Configuration de la base de données SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///quiz_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration CORS pour permettre les requêtes depuis Flutter
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    """Configuration pour le développement"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration pour la production"""
    DEBUG = False

# Configuration par défaut
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}