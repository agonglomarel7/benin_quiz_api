from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_my_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"success": False, "message": "Utilisateur non trouvé"}), 404

    return jsonify({
        "success": True,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
            # ajoute d'autres champs si nécessaire
        }
    }), 200
