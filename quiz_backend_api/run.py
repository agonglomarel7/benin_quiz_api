from app import create_app
import os

# Créer l'application Flask
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    # Lancer l'application en mode développement
    app.run(
        host='0.0.0.0',  # Accessible depuis n'importe quelle adresse
        port=5000,       # Port 5000
        debug=True       # Mode debug activé
    )