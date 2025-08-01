from flask import request, jsonify
from models.question import Question
from models.category import Category
from database import db

class QuestionController:

    @staticmethod
    def creer():
        try:
            data = request.get_json()
            texte = data.get('texte')
            category_id = data.get('category_id')

            if not texte or not category_id:
                return jsonify({'erreur': 'Texte et category_id requis'}), 400

            # Vérifier si la catégorie existe
            if not Category.query.get(category_id):
                return jsonify({'erreur': 'Catégorie non trouvée'}), 404

            question = Question(texte=texte, category_id=category_id)
            db.session.add(question)
            db.session.commit()

            return jsonify({'message': 'Question créée', 'question': question.to_dict()}), 201
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500

    @staticmethod
    def lister_par_categorie(category_id):
        try:
            questions = Question.query.filter_by(category_id=category_id).all()
            return jsonify([q.to_dict() for q in questions]), 200
        except Exception as e:
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500
