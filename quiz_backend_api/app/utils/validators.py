import re
from email_validator import validate_email, EmailNotValidError

def validate_signup_data(data):
    """
    Valider les données d'inscription
    
    Args:
        data (dict): Données à valider
        
    Returns:
        tuple: (is_valid, errors)
    """
    errors = []
    
    # Vérifier la présence des champs obligatoires
    required_fields = ['username', 'email', 'password']
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f'Le champ {field} est obligatoire')
    
    if errors:
        return False, errors
    
    # Validation du nom d'utilisateur
    username = data['username'].strip()
    if len(username) < 3:
        errors.append('Le nom d\'utilisateur doit contenir au moins 3 caractères')
    elif len(username) > 80:
        errors.append('Le nom d\'utilisateur ne peut pas dépasser 80 caractères')
    elif not re.match(r'^[a-zA-Z0-9_]+$', username):
        errors.append('Le nom d\'utilisateur ne peut contenir que des lettres, chiffres et underscores')
    
    # Validation de l'email
    try:
        validate_email(data['email'])
    except EmailNotValidError:
        errors.append('Format d\'email invalide')
    
    # Validation du mot de passe
    password = data['password']
    if len(password) < 6:
        errors.append('Le mot de passe doit contenir au moins 6 caractères')
    elif len(password) > 255:
        errors.append('Le mot de passe ne peut pas dépasser 255 caractères')
    
    return len(errors) == 0, errors