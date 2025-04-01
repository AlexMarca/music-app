from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user,logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exists


auth_bp = Blueprint('auth_bp', __name__)

# Route de connexion
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    from model import User
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main_bp.index'))

        flash('Identifiants incorrects', 'danger')
    return render_template('login.html')

# Route d'inscription
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    from app import db
    from model import User
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        # Verification de l'existance de l'utilisateur via mail 
        exists_query_mail = db.session.query(exists().where(User.email == email)).scalar()
        if exists_query_mail:
            flash('Cette adresse e-mail est déjà utilisée. Veuillez en choisir une autre.')
            return redirect(url_for('auth_bp.signup'))
        
        # Verification de l'existance de l'utilisateur via username    
        exists_query_username = db.session.query(exists().where(User.username == username)).scalar()
        if exists_query_username :
            flash("Ce nom d'utilisateur est déjà utilisée. Veuillez en choisir une autre.")
            return redirect(url_for('auth_bp.signup'))
        
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Inscription réussie", 'success')
        return redirect(url_for('main_bp.index'))

    return render_template('signup.html')

# Route de déconnexion
@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
