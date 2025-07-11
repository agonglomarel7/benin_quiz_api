# 🎯 Quiz App Backend - Flask API

Une API REST Flask avec architecture MVC pour gérer les utilisateurs d'une application de quiz mobile développée avec Flutter.

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Technologies utilisées](#️-technologies-utilisées)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [Utilisation](#-utilisation)
- [API Endpoints](#-api-endpoints)
- [Architecture](#️-architecture)
- [Tests](#-tests)
- [Déploiement](#-déploiement)
- [Contribution](#-contribution)
- [Licence](#-licence)

## ✨ Fonctionnalités

- 🔐 **Inscription d'utilisateurs** avec validation complète
- 🛡️ **Hashage sécurisé** des mots de passe
- ✅ **Validation des données** (email, nom d'utilisateur, mot de passe)
- 🚫 **Prévention des doublons** (email et nom d'utilisateur uniques)
- 🌐 **API REST** avec réponses JSON
- 🔄 **CORS** activé pour les applications Flutter
- 📊 **Architecture MVC** claire et maintenable
- 🗄️ **Base de données SQLite** (facile à configurer)

## 🛠️ Technologies utilisées

- **Flask** 2.3.3 - Framework web Python
- **SQLAlchemy** 3.0.5 - ORM pour la base de données
- **Flask-CORS** 4.0.0 - Gestion des requêtes cross-origin
- **Werkzeug** 2.3.7 - Hashage sécurisé des mots de passe
- **SQLite** - Base de données légère
- **Python** 3.8+ - Langage de programmation

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.8+** ([Télécharger Python](https://www.python.org/downloads/))
- **pip** (gestionnaire de paquets Python)
- **Git** ([Télécharger Git](https://git-scm.com/))

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-username/quiz-backend.git
cd quiz-backend
```

### 2. Créer un environnement virtuel

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate

# Sur macOS/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Structure du projet

```
quiz_backend/
├── app/
│   ├── __init__.py           # Configuration Flask
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py           # Modèle utilisateur
│   ├── views/
│   │   ├── __init__.py
│   │   └── auth.py           # Routes d'authentification
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── auth_controller.py # Logique métier
│   └── utils/
│       ├── __init__.py
│       └── validators.py      # Validation des données
├── config.py                 # Configuration de l'app
├── requirements.txt          # Dépendances Python
├── run.py                   # Point d'entrée de l'application
└── README.md                # Ce fichier
```

## ⚙️ Configuration

### Variables d'environnement

Créez un fichier `.env` à la racine du projet :

```env
SECRET_KEY=votre-cle-secrete-ultra-securisee
FLASK_ENV=development
DATABASE_URL=sqlite:///quiz_app.db
```

### Configuration de base

Le fichier `config.py` contient les configurations pour :
- 🔑 **Clé secrète** pour les sessions
- 🗄️ **Base de données** SQLite
- 🌐 **CORS** pour Flutter
- 🐛 **Mode debug** pour le développement

## 🏃‍♂️ Utilisation

### Lancer l'application

```bash
# Activer l'environnement virtuel
source venv/bin/activate  # ou venv\Scripts\activate sur Windows

# Lancer l'application
python run.py
```

L'API sera accessible sur : `http://localhost:5000`

### Vérifier que l'API fonctionne

```bash
curl -X GET http://localhost:5000/api/auth/test
```

Réponse attendue :
```json
{
  "success": true,
  "message": "API de quiz fonctionne correctement!"
}
```

## 🔌 API Endpoints

### Authentification

#### `POST /api/auth/signup`
Créer un nouveau compte utilisateur.

**Requête :**
```json
{
  "username": "nom_utilisateur",
  "email": "email@example.com",
  "password": "motdepasse123"
}
```

**Réponse de succès (201) :**
```json
{
  "success": true,
  "message": "Compte créé avec succès!",
  "user": {
    "id": 1,
    "username": "nom_utilisateur",
    "email": "email@example.com",
    "created_at": "2024-01-15T10:30:00.000000",
    "is_active": true
  }
}
```

**Réponse d'erreur (400) :**
```json
{
  "success": false,
  "message": "Données invalides",
  "errors": [
    "Le nom d'utilisateur doit contenir au moins 3 caractères"
  ]
}
```

#### `GET /api/auth/user/<id>`
Récupérer les informations d'un utilisateur.

**Réponse de succès (200) :**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "username": "nom_utilisateur",
    "email": "email@example.com",
    "created_at": "2024-01-15T10:30:00.000000",
    "is_active": true
  }
}
```

#### `GET /api/auth/test`
Endpoint de test pour vérifier le fonctionnement de l'API.

## 🏗️ Architecture

### Modèle MVC

- **📊 Models** (`app/models/`) : Gestion des données et base de données
- **🖥️ Views** (`app/views/`) : Routes et endpoints API
- **🎮 Controllers** (`app/controllers/`) : Logique métier et traitement des données
- **🔧 Utils** (`app/utils/`) : Fonctions utilitaires et validation

### Sécurité

- 🔒 **Hashage des mots de passe** avec Werkzeug
- ✅ **Validation stricte** des données d'entrée
- 🛡️ **Gestion des erreurs** sans fuite d'information
- 🚫 **Protection contre les doublons** (email et username uniques)

## 🧪 Tests

### Tester avec cURL

```bash
# Test d'inscription
curl -X POST http://localhost:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "motdepasse123"
  }'
```

### Tester avec Postman

1. Importez la collection Postman (si disponible)
2. Configurez l'URL de base : `http://localhost:5000`
3. Testez les endpoints avec différents cas de test

### Intégration avec Flutter

```dart
// Exemple d'appel API depuis Flutter
Future<Map<String, dynamic>> signUp(String username, String email, String password) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/api/auth/signup'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'username': username,
      'email': email,
      'password': password,
    }),
  );
  
  return jsonDecode(response.body);
}
```

## 🚀 Déploiement

### Déploiement local

```bash
# Configurer pour la production
export FLASK_ENV=production

# Lancer avec Gunicorn (recommandé)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Déploiement sur Heroku

1. Créez un fichier `Procfile` :
```
web: gunicorn run:app
```

2. Ajoutez `gunicorn` au `requirements.txt`

3. Déployez :
```bash
heroku create votre-app-name
git push heroku main
```

### Déploiement sur Railway/Render

Suivez la documentation de votre plateforme de choix.

## 📈 Prochaines étapes

- [ ] 🔐 **Authentification JWT** pour sécuriser les sessions
- [ ] 🚪 **Endpoint de connexion** (login)
- [ ] 📝 **Gestion des quiz** (CRUD)
- [ ] 🏆 **Système de scores** et classements
- [ ] 🧪 **Tests unitaires** avec pytest
- [ ] 📚 **Documentation API** avec Swagger
- [ ] 🔄 **Refresh tokens** pour la sécurité
- [ ] 📧 **Vérification d'email** à l'inscription

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Fork** le projet
2. **Créez** une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. **Committez** vos changements (`git commit -m 'Ajouter une nouvelle fonctionnalité'`)
4. **Pushez** vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. **Ouvrez** une Pull Request

### Standards de code

- Suivez les conventions **PEP 8** pour Python
- Ajoutez des **commentaires** pour expliquer la logique complexe
- Écrivez des **tests** pour les nouvelles fonctionnalités
- Mettez à jour la **documentation** si nécessaire

## 📞 Support

Si vous avez des questions ou des problèmes :

1. **Vérifiez** les [Issues existantes](https://github.com/votre-username/quiz-backend/issues)
2. **Créez** une nouvelle issue si nécessaire
3. **Contactez** l'équipe de développement

## 🔧 Dépannage

### Erreurs communes

**Erreur : `ModuleNotFoundError`**
```bash
# Vérifiez que l'environnement virtuel est activé
source venv/bin/activate
pip install -r requirements.txt
```

**Erreur : `Port already in use`**
```bash
# Changez le port dans run.py ou tuez le processus
lsof -ti:5000 | xargs kill -9
```

**Erreur de base de données**
```bash
# Supprimez la base de données et relancez
rm quiz_app.db
python run.py
```

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 🎉 Remerciements

Merci d'utiliser Quiz App Backend ! Si ce projet vous aide, n'hésitez pas à lui donner une ⭐ sur GitHub.

**Développé avec ❤️ pour la communauté Flutter & Python**
