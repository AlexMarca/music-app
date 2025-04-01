from flask import Flask
from config import Config
from flask_login import LoginManager
from extension import db  # Importe l'instance unique de SQLAlchemy

# Initialisation de l'application
app = Flask(__name__)
app.config.from_object(Config)

# Initialiser l'extension SQLAlchemy
db.init_app(app)

from routes.auth_routes import auth_bp
from routes.main_routes import main_bp

with app.app_context():
    db.create_all()
# Initialisation de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_bp.login'  # Route de login pour Flask-Login

# Enregistrement des Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)

# Charger l'utilisateur pour Flask-Login
@login_manager.user_loader
def load_user(user_id):
    from model import User
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)
