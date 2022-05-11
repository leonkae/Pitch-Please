from flask import render_template,redirect,url_for
from . import main_blueprint as main
from flask_login import login_required
from .forms import PitchForm
from .models import Pitches
from app import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pitches')
@login_required
def pitches():
    return render_template('pitches.html')


@main.route('/pitches/add', methods=['GET', 'POST'])
@login_required
def createPitch():
    create_pitch=PitchForm()
    if create_pitch.validate_on_submit():
        pitch = Pitches(title=create_pitch.title.data, body=create_pitch.body.data, category=create_pitch.category.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main_blueprint.pitches'))
    return render_template('createpitch.html',create=create_pitch)
