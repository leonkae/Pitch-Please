from flask import render_template,redirect,url_for
from . import main_blueprint as main
from flask_login import login_required
from .forms import PitchForm,CommentForm
from .models import Pitches,Comments
from app import db




@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pitches')
@login_required
def pitches():
    pitches = Pitches.query.all()
    # print(pitches)
    form = CommentForm()
    return render_template('pitches.html',pitches=pitches, comment_form=form)


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

@main.route('/comment/<int:pitch_id>/add', methods=['POST'])
@login_required
def add_comment(pitch_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comments(comment=form.comment.data, pitch_id = pitch_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main_blueprint.pitches',pitch_id=pitch_id))
    return render_template('pitches.html',comment_form=form)

# @main.route('/account')
# @login_required
# def acoount():
#     image_file = url_for('static' ,filename='app/')