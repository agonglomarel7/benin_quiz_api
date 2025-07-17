from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

class UserController:
    """Contrôleur pour gérer les profils utilisateurs"""
    
    @staticmethod
    @jwt_required()
    def profil():
        """Récupérer le profil de l'utilisateur connecté"""
        try:
            # Récupération de l'ID utilisateur depuis le token JWT
            user_id = get_jwt_identity()
            
            # Recherche de l'utilisateur
            utilisateur = User.query.get(user_id)
            
            if not utilisateur:
                return jsonify({'erreur': 'Utilisateur non trouvé'}), 404
            
            return jsonify({
                'utilisateur': utilisateur.to_dict()
            }), 200
            
        except Exception as e:
            print(f"Erreur lors de la récupération du profil: {str(e)}")  # Pour le debug
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500
