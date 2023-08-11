from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
config = os.path.join(app.config.get('ROOT_DIR', os.getcwd()), 'config.py')
app.config.from_pyfile(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from hackathon.models import SignUp, DietaryRestrictions, Pronouns, Race

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('registration.html')
    form_data = request.form.to_dict()
    new_signup = SignUp(form_data)
    new_dietary = DietaryRestrictions(form_data, new_signup.id)
    pronouns = Pronouns(form_data, new_signup.id)
    race = Race(form_data, new_signup.id)
    db.session.add(new_signup)
    db.session.add(new_dietary)
    db.session.add(pronouns)
    db.session.add(race)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/favicon/<string:filename>')
def favicon(filename):
    return send_from_directory('favicon', filename)

@app.route('/static/<string:filename>')
def static_dir(filename):
    return send_from_directory('static', filename)
