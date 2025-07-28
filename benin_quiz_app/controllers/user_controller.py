# ========== controllers/user_controller.py (corrigé) ==========
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models.user import User

class UserController:
    """Contrôleur pour gérer les profils utilisateurs"""
    
    @staticmethod
    def profil():  # ← Plus de @jwt_required() ici
        """Récupérer le profil de l'utilisateur connecté"""
        try:
            # Récupération de l'ID utilisateur depuis le token JWT
            user_id = get_jwt_identity()
            
            # S'assurer que user_id est un entier (peu importe le type dans le token)
            user_id = int(user_id)
            
            # Recherche de l'utilisateur
            utilisateur = User.query.get(user_id)
            
            if not utilisateur:
                return jsonify({'erreur': 'Utilisateur non trouvé'}), 404
            
            return jsonify({
                'message': 'Profil récupéré avec succès',
                'utilisateur': utilisateur.to_dict()
            }), 200
            
        except Exception as e:
            print(f"Erreur lors de la récupération du profil: {str(e)}")  # Pour le debug
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500
        