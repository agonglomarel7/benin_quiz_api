from flask import Blueprint
from controllers.question_controller import QuestionController

question_bp = Blueprint('question', __name__, url_prefix='/api/questions')

question_bp.route('', methods=['POST'])(QuestionController.creer)
question_bp.route('/categorie/<int:category_id>', methods=['GET'])(QuestionController.lister_par_categorie)
