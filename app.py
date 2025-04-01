from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialisation de Flask
app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'ta_clé_secrète'  # Nécessaire pour gérer les sessions et sécuriser les cookies
db = SQLAlchemy(app)

# Initialisation de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté

# Modèle utilisateur
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Créer la base de données si elle n'existe pas
with app.app_context():
    db.create_all()
    
# Chargement de l'utilisateur connecté
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Rechercher l'utilisateur dans la base de données
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            # Connexion réussie
            login_user(user)
            return redirect(url_for('index'))  # Rediriger vers la page d'accueil
        else:
            flash('Identifiants incorrects, réessayez.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required  # Assure que l'utilisateur est bien connecté avant de pouvoir se déconnecter
def logout():
    logout_user()  # Déconnexion
    return redirect(url_for('login'))  # Rediriger vers la page de connexion après la déconnexion

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Vérifier si l'email ou le nom d'utilisateur est déjà utilisé
        user_by_email = User.query.filter_by(email=email).first()
        user_by_username = User.query.filter_by(username=username).first()
        if user_by_email or user_by_username:
            flash("L'email ou le nom d'utilisateur est déjà utilisé.", 'danger')
            return redirect(url_for('signup'))

        # Hacher le mot de passe et créer un nouvel utilisateur
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Inscription réussie ! Vous pouvez maintenant vous connecter.", 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Route pour la page des exercices
@app.route('/exercice')
def exercice():
    return render_template('exercice.html')

# Route pour la page des paramètres
@app.route('/parametres')
def parametres():
    return render_template('parametres.html')
# Page d'accueil (index)
@app.route('/')
@login_required  # Protection de cette route, l'utilisateur doit être connecté
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)