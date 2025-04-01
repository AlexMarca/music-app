from functools import wraps
from flask import abort
from flask_login import current_user

def roles_required(*roles):
    """
    Permet d'accéder à la vue uniquement si l'utilisateur a l'un des rôles spécifiés.
    Exemples d'utilisation :
      @roles_required('admin')
      @roles_required('admin', 'moderator')
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                # L'utilisateur n'est pas connecté
                abort(403)
            if current_user.role not in roles:
                # L'utilisateur n'a pas le rôle requis
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
