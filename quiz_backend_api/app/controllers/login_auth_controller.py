from werkzeug.security import check_password_hash
from flask import jsonify
from app.models.user import User

class AuthController:
    ...

    @staticmethod
    def login(data):
        """
        Logique de connexion utilisateur
        
        Args:
            data (dict): Données de connexion (username ou email, password)
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            # Vérifier que les champs sont bien là
            if 'username' not in data or 'password' not in data:
                return {
                    'success': False,
                    'message': 'Nom d\'utilisateur et mot de passe requis'
                }, 400
            
            username = data['username']
            password = data['password']

            # Rechercher l'utilisateur par username ou email
            user = User.query.filter_by(username=username).first()
            if not user:
                return {
                    'success': False,
                    'message': 'Utilisateur non trouvé'
                }, 404

            # Vérifier le mot de passe
            if not user.check_password(password):
                return {
                    'success': False,
                    'message': 'Mot de passe incorrect'
                }, 401

            # Connexion réussie
            return {
                'success': True,
                'message': 'Connexion réussie',
                'user': user.to_dict()
            }, 200

        except Exception as e:
            return {
                'success': False,
                'message': 'Erreur serveur lors de la connexion',
                'error': str(e)
            }, 500
