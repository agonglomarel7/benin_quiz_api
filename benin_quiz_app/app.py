# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta

# Déclaration des extensions
from models.user import db  # ✅ C'est ici que tu centralises db

jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    
    # Configuration de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///benin_quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configuration JWT pour l'authentification
    app.config['JWT_SECRET_KEY'] = 'votre-cle-secrete-changez-la-en-production'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
    
    # Initialisation des extensions avec l'app
    db.init_app(app)
    jwt.init_app(app)
    
    # Import des modèles après l'initialisation
    
    # Import et enregistrement des routes
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    
    # Création des tables au démarrage
    with app.app_context():
        from models.user import User 
        db.create_all()
        print("Base de données créée avec succès!")
    
    return app

# ✅ Add this line - create the app instance for gunicorn
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)