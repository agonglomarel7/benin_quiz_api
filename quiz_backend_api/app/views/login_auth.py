from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__)  # ✅ Blueprint correctement défini

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint pour la connexion d'un utilisateur
    {
        "username": "nom_utilisateur",
        "password": "mot_de_passe"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'Aucune donnée reçue'}), 400

        response_data, status_code = AuthController.login(data)
        return jsonify(response_data), status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Erreur serveur',
            'error': str(e)
        }), 500


