# routes/category_routes.py
from flask import Blueprint
from controllers.categoryController import CategoryController

category_bp = Blueprint('category', __name__, url_prefix='/api/categories')

category_bp.route('', methods=['POST'])(CategoryController.creer)
category_bp.route('', methods=['GET'])(CategoryController.lister)
