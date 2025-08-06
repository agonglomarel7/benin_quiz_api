from flask import Blueprint
from controllers.reponse_controller import ReponseController

reponse_bp = Blueprint('reponse', __name__, url_prefix='/api/reponses')

reponse_bp.route('', methods=['POST'])(ReponseController.ajouter)
reponse_bp.route('/question/<int:question_id>', methods=['GET'])(ReponseController.lister_par_question)
