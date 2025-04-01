from flask import Flask, render_template

app = Flask(__name__)

# Route pour le menu principal
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la page des exercices
@app.route('/exercice')
def exercice():
    return render_template('exercice.html')

# Route pour la page des paramètres
@app.route('/parametres')
def parametres():
    return render_template('parametres.html')

if __name__ == "__main__":
    app.run(debug=True)
