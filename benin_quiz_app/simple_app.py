from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import re

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///benin_quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'votre-cle-secrete-changez-la-en-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# Initialisation des extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Modèle User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    pseudo = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe_hash = db.Column(db.String(255), nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, nom, prenom, pseudo, email, mot_de_passe):
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.mot_de_passe_hash = generate_password_hash(mot_de_passe)
    
    def verifier_mot_de_passe(self, mot_de_passe):
        return check_password_hash(self.mot_de_passe_hash, mot_de_passe)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'pseudo': self.pseudo,
            'email': self.email,
            'date_creation': self.date_creation.isoformat() if self.date_creation else None
        }

# Fonction pour valider l'email
def valider_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Route d'inscription
@app.route('/api/auth/inscription', methods=['POST'])
def inscription():
    try:
        data = request.get_json()
        print(f"Données reçues: {data}")  # Debug
        
        # Vérification des champs requis
        champs_requis = ['nom', 'prenom', 'pseudo', 'email', 'mot_de_passe']
        for champ in champs_requis:
            if not data.get(champ):
                return jsonify({'erreur': f'Le champ {champ} est requis'}), 400
        
        # Validation de l'email
        if not valider_email(data['email']):
            return jsonify({'erreur': 'Format email invalide'}), 400
        
        # Vérification unicité pseudo
        if User.query.filter_by(pseudo=data['pseudo']).first():
            return jsonify({'erreur': 'Ce pseudo est déjà utilisé'}), 400
        
        # Vérification unicité email
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'erreur': 'Cet email est déjà utilisé'}), 400
        
        # Création de l'utilisateur
        nouvel_utilisateur = User(
            nom=data['nom'],
            prenom=data['prenom'],
            pseudo=data['pseudo'],
            email=data['email'],
            mot_de_passe=data['mot_de_passe']
        )
        
        # Sauvegarde
        db.session.add(nouvel_utilisateur)
        db.session.commit()
        print(f"Utilisateur créé avec succès: {nouvel_utilisateur.pseudo}")  # Debug
        
        # Création du token
        token = create_access_token(identity=nouvel_utilisateur.id)
        
        return jsonify({
            'message': 'Inscription réussie',
            'token': token,
            'utilisateur': nouvel_utilisateur.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de l'inscription: {str(e)}")
        return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500

# Route de connexion
@app.route('/api/auth/connexion', methods=['POST'])
def connexion():
    try:
        data = request.get_json()
        print(f"Tentative de connexion: {data.get('pseudo')}")  # Debug
        
        # Vérification des champs requis
        if not data.get('pseudo') or not data.get('mot_de_passe'):
            return jsonify({'erreur': 'Pseudo et mot de passe requis'}), 400
        
        # Recherche de l'utilisateur
        utilisateur = User.query.filter_by(pseudo=data['pseudo']).first()
        
        # Vérification
        if not utilisateur or not utilisateur.verifier_mot_de_passe(data['mot_de_passe']):
            return jsonify({'erreur': 'Pseudo ou mot de passe incorrect'}), 401
        
        # Création du token
        token = create_access_token(identity=utilisateur.id)
        
        return jsonify({
            'message': 'Connexion réussie',
            'token': token,
            'utilisateur': utilisateur.to_dict()
        }), 200
        
    except Exception as e:
        print(f"Erreur lors de la connexion: {str(e)}")
        return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500

# Route pour récupérer le profil
@app.route('/api/user/profil', methods=['GET'])
@jwt_required()
def profil():
    try:
        user_id = get_jwt_identity()
        utilisateur = User.query.get(user_id)
        
        if not utilisateur:
            return jsonify({'erreur': 'Utilisateur non trouvé'}), 404
        
        return jsonify({
            'utilisateur': utilisateur.to_dict()
        }), 200
        
    except Exception as e:
        print(f"Erreur lors de la récupération du profil: {str(e)}")
        return jsonify({'erreur': f'Erreur serveur: {str(e)}'}), 500

# Route de test pour vérifier que l'API fonctionne
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'API Benin Quiz fonctionne!'}), 200

# Création des tables
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Base de données créée avec succès!")
        print("✅ Serveur prêt sur http://localhost:5000")
        print("✅ Testez avec: curl http://localhost:5000/api/test")
    
    app.run(debug=True)