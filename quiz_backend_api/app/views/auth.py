
from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import AuthController

# Création d'un blueprint pour les routes d'authentification
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    """
    Endpoint pour l'inscription d'un nouvel utilisateur
    
    Expected JSON:
    {
        "username": "nom_utilisateur",
        "email": "email@example.com",
        "password": "mot_de_passe"
    }
    """
    try:
        # Récupérer les données JSON de la requête
        data = request.get_json()
        
        # Vérifier que les données sont présentes
        if not data:
            return jsonify({
                'success': False,
                'message': 'Aucune donnée reçue'
            }), 400
        
        # Appeler le contrôleur pour traiter l'inscription
        response_data, status_code = AuthController.signup(data)
        
        # Retourner la réponse JSON
        return jsonify(response_data), status_code
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Erreur serveur',
            'error': str(e)
        }), 500

@auth_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Endpoint pour récupérer les informations d'un utilisateur"""
    try:
        response_data, status_code = AuthController.get_user_by_id(user_id)
        return jsonify(response_data), status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Erreur serveur',
            'error': str(e)
        }), 500

@auth_bp.route('/test', methods=['GET'])
def test():
    """Endpoint de test pour vérifier que l'API fonctionne"""
    return jsonify({
        'success': True,
        'message': 'API de quiz fonctionne correctement!'
    }), 200