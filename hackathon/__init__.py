from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
config = os.path.join(app.config.get('ROOT_DIR', os.getcwd()), 'config.py')
app.config.from_pyfile(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from hackathon.models import SignUp, DietaryRestrictions, Race, Orientation, Major, Photo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('registration.html')
    try:
        form_data = request.get_json(force=True)
        new_signup = SignUp(form_data)
        db.session.add(new_signup)
        db.session.commit()
        dietary = DietaryRestrictions(form_data, new_signup.id)
        race = Race(form_data, new_signup.id)
        orientation = Orientation(form_data, new_signup.id)
        major = Major(form_data, new_signup.id)
        photo = Photo(form_data, new_signup.id)

        db.session.add(dietary)
        db.session.add(race)
        db.session.add(orientation)
        db.session.add(major)
        db.session.add(photo)
        db.session.commit()
        return f'{new_signup.id}', 200
    except ValueError as value_err:
        return str(value_err), 400

@app.route('/success')
def success():
    return render_template('success.html', reg_id=request.args['id'])

@app.route('/favicon/<string:filename>')
def favicon(filename):
    return send_from_directory('favicon', filename)

@app.route('/static/<string:filename>')
def static_dir(filename):
    return send_from_directory('static', filename)
