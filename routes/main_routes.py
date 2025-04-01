from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint('main_bp', __name__)

# Page d'accueil (index)
@main_bp.route('/')
@login_required
def index():
    return render_template('index.html')

# Page de l'exercice musical
@main_bp.route('/exercice')
@login_required
def exercice():
    return render_template('exercice.html')

# Page des paramètres
@main_bp.route('/parametres')
@login_required
def parametres():
    return render_template('parametres.html')
