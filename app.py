from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_exercise')
def get_exercise():
    exercise = {
        "notes": ["C/4", "D/4", "E/4", "F/4", "G/4"]  # Do, Ré, Mi, Fa, Sol
    }
    return jsonify(exercise)

if __name__ == '__main__':
    app.run(debug=True)
