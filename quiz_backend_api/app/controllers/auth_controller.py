from flask import jsonify
from app import db
from app.models.user import User
from app.utils.validators import validate_signup_data

class AuthController:
    """Contrôleur pour gérer l'authentification"""
    
    @staticmethod
    def signup(data):
        """
        Logique pour créer un nouveau compte utilisateur
        
        Args:
            data (dict): Données d'inscription (username, email, password)
            
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            # 1. Validation des données
            is_valid, errors = validate_signup_data(data)
            if not is_valid:
                return {
                    'success': False,
                    'message': 'Données invalides',
                    'errors': errors
                }, 400
            
            # 2. Vérifier si l'utilisateur existe déjà
            existing_user = User.query.filter(
                (User.username == data['username']) | 
                (User.email == data['email'])
            ).first()
            
            if existing_user:
                return {
                    'success': False,
                    'message': 'Un utilisateur avec ce nom ou cet email existe déjà'
                }, 409
            
            # 3. Créer le nouvel utilisateur
            new_user = User(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            
            # 4. Sauvegarder en base de données
            db.session.add(new_user)
            db.session.commit()
            
            # 5. Retourner la réponse de succès
            return {
                'success': True,
                'message': 'Compte créé avec succès!',
                'user': new_user.to_dict()
            }, 201
            
        except Exception as e:
            # En cas d'erreur, annuler la transaction
            db.session.rollback()
            return {
                'success': False,
                'message': 'Erreur lors de la création du compte',
                'error': str(e)
            }, 500
    
    @staticmethod
    def get_user_by_id(user_id):
        """Récupérer un utilisateur par son ID"""
        try:
            user = User.query.get(user_id)
            if user:
                return {
                    'success': True,
                    'user': user.to_dict()
                }, 200
            else:
                return {
                    'success': False,
                    'message': 'Utilisateur non trouvé'
                }, 404
        except Exception as e:
            return {
                'success': False,
                'message': 'Erreur lors de la récupération de l\'utilisateur',
                'error': str(e)
            }, 500