from flask import request, jsonify
from models.user import User
from app import db
from flask_jwt_extended import create_access_token
import re

class AuthController:
    """Contrôleur pour gérer l'authentification"""
    
    @staticmethod
    def valider_email(email):
        """Valider le format de l'email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def inscription():
        """Créer un nouveau compte utilisateur"""
        try:
            # Récupération des données envoyées
            data = request.get_json()
            
            # Vérification que tous les champs sont présents
            champs_requis = ['nom', 'prenom', 'pseudo', 'email', 'mot_de_passe']
            for champ in champs_requis:
                if not data.get(champ):
                    return jsonify({'erreur': f'Le champ {champ} est requis'}), 400
            
            # Validation de l'email
            if not AuthController.valider_email(data['email']):
                return jsonify({'erreur': 'Format email invalide'}), 400
            
            # Vérification que le pseudo n'existe pas déjà
            if User.query.filter_by(pseudo=data['pseudo']).first():
                return jsonify({'erreur': 'Ce pseudo est déjà utilisé'}), 400
            
            # Vérification que l'email n'existe pas déjà
            if User.query.filter_by(email=data['email']).first():
                return jsonify({'erreur': 'Cet email est déjà utilisé'}), 400
            
            # Création du nouvel utilisateur
            nouvel_utilisateur = User(
                nom=data['nom'],
                prenom=data['prenom'],
                pseudo=data['pseudo'],
                email=data['email'],
                mot_de_passe=data['mot_de_passe']
            )
            
            # Sauvegarde en base de données
            db.session.add(nouvel_utilisateur)
            db.session.commit()
            
            # Création du token JWT
            token = create_access_token(identity=nouvel_utilisateur.id)
            
            return jsonify({
                'message': 'Inscription réussie',
                'token': token,
                'utilisateur': nouvel_utilisateur.to_dict()
            }), 201
            
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors de l'inscription: {str(e)}")  # Pour le debug
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500
    
    @staticmethod
    def connexion():
        """Connecter un utilisateur existant"""
        try:
            # Récupération des données
            data = request.get_json()
            
            # Vérification des champs requis
            if not data.get('pseudo') or not data.get('mot_de_passe'):
                return jsonify({'erreur': 'Pseudo et mot de passe requis'}), 400
            
            # Recherche de l'utilisateur
            utilisateur = User.query.filter_by(pseudo=data['pseudo']).first()
            
            # Vérification de l'existence et du mot de passe
            if not utilisateur or not utilisateur.verifier_mot_de_passe(data['mot_de_passe']):
                return jsonify({'erreur': 'Pseudo ou mot de passe incorrect'}), 401
            
            # Création du token JWT
            token = create_access_token(identity=utilisateur.id)
            
            return jsonify({
                'message': 'Connexion réussie',
                'token': token,
                'utilisateur': utilisateur.to_dict()
            }), 200
            
        except Exception as e:
            print(f"Erreur lors de la connexion: {str(e)}")  # Pour le debug
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500
