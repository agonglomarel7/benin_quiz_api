from flask import Blueprint
from controllers.user_controller import UserController

# Création du blueprint pour les routes utilisateur
user_bp = Blueprint('user', __name__)

# Route pour récupérer le profil
@user_bp.route('/profil', methods=['GET'])
def profil():
    """Route GET pour récupérer le profil utilisateur"""
    return UserController.profil()