# ========== routes/auth_routes.py (Routes d'authentification) ==========
from flask import Blueprint
from controllers.auth_controller import AuthController

# Création du blueprint pour les routes d'authentification
auth_bp = Blueprint('auth', __name__)

# Route pour l'inscription
@auth_bp.route('/inscription', methods=['POST'])
def inscription():
    """Route POST pour créer un nouveau compte"""
    return AuthController.inscription()

# Route pour la connexion
@auth_bp.route('/connexion', methods=['POST'])
def connexion():
    """Route POST pour se connecter"""
    return AuthController.connexion()