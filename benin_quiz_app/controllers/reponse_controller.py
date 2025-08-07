from flask import request, jsonify
from models.reponse import Reponse
from models.question import Question
from database import db

class ReponseController:

    @staticmethod
    def ajouter():
        try:
            data = request.get_json()
            texte = data.get('texte')
            est_correcte = data.get('est_correcte', False)
            question_id = data.get('question_id')

            if not texte or question_id is None:
                return jsonify({'erreur': 'Texte et question_id requis'}), 400

            if not Question.query.get(question_id):
                return jsonify({'erreur': 'Question non trouvée'}), 404

            reponse = Reponse(texte=texte, est_correcte=est_correcte, question_id=question_id)
            db.session.add(reponse)
            db.session.commit()

            return jsonify({'message': 'Réponse ajoutée', 'reponse': reponse.to_dict()}), 201
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500

    @staticmethod
    def lister_par_question(question_id):
        try:
            reponses = Reponse.query.filter_by(question_id=question_id).all()
            return jsonify([r.to_dict() for r in reponses]), 200
        except Exception as e:
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500
