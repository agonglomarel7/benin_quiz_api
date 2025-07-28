
# ========== routes/user_routes.py (corrigé) ==========
from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController

# Création du blueprint pour les routes utilisateur
user_bp = Blueprint('user', __name__)

# Route pour récupérer le profil
@user_bp.route('/profil', methods=['GET'])
@jwt_required()  # ← Le décorateur JWT doit être ici !
def profil():
    """Route GET pour récupérer le profil utilisateur"""
    return UserController.profil()