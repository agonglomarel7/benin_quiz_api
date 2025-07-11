from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """Modèle pour représenter un utilisateur dans la base de données"""
    
    # Définition des colonnes de la table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __init__(self, username, email, password):
        """Constructeur pour créer un nouvel utilisateur"""
        self.username = username
        self.email = email
        self.set_password(password)
    
    def set_password(self, password):
        """Hasher le mot de passe avant de le stocker"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Vérifier si le mot de passe est correct"""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convertir l'objet utilisateur en dictionnaire (pour JSON)"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
    
    def __repr__(self):
        """Représentation string de l'utilisateur"""
        return f'<User {self.username}>'