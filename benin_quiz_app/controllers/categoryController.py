# controllers/category_controller.py
from flask import request, jsonify
from models.category import Category
from database import db

class CategoryController:
    
    @staticmethod
    def creer():
        try:
            data = request.get_json()
            nom = data.get('nom')
            description = data.get('description')
            icone = data.get('icone')

            if not nom:
                return jsonify({'erreur': 'Le nom est requis'}), 400
            
            if Category.query.filter_by(nom=nom).first():
                return jsonify({'erreur': 'La catégorie existe déjà'}), 400
            
            categorie = Category(nom=nom, description=description, icone=icone)
            db.session.add(categorie)
            db.session.commit()

            return jsonify({'message': 'Catégorie créée avec succès', 'categorie': categorie.to_dict()}), 201
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500

    @staticmethod
    def lister():
        try:
            categories = Category.query.all()
            return jsonify([cat.to_dict() for cat in categories]), 200
        except Exception as e:
            return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500
