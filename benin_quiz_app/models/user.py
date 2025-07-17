from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # ← On déclare ici, mais on l'initialise dans app.py

class User(db.Model):
    """Modèle pour représenter un utilisateur du quiz"""
    
    # Définition des colonnes de la table
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    pseudo = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe_hash = db.Column(db.String(255), nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, nom, prenom, pseudo, email, mot_de_passe):
        """Constructeur pour créer un nouvel utilisateur"""
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.mot_de_passe_hash = generate_password_hash(mot_de_passe)
    
    def verifier_mot_de_passe(self, mot_de_passe):
        """Vérifier si le mot de passe est correct"""
        return check_password_hash(self.mot_de_passe_hash, mot_de_passe)
    
    def to_dict(self):
        """Convertir l'utilisateur en dictionnaire (pour JSON)"""
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'pseudo': self.pseudo,
            'email': self.email,
            'date_creation': self.date_creation.isoformat() if self.date_creation else None
        }