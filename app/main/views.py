from flask import render_template,redirect,url_for,request
from . import main_blueprint as main
from flask_login import login_required
from .forms import PitchForm,CommentForm,UpdateAccount
from .models import Pitches,Comments,User
from app import db,photos





@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pitches')
@login_required
def pitches():
    # user = User.query.filter_by(username = uname).first()
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

@main.route('/account/<uname>')
@login_required
def account(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template('account.html',user=user)

@main.route('/account/<uname>/update/',methods= ['GET', 'POST'])
@login_required
def update_account(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    update = UpdateAccount()   
    if update.validate_on_submit():
        user.bio = update.bio.data
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.account',uname=user.username))
    return render_template('update.html',update=update)
        
@main.route('/account/<uname>/update/pic', methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    
    return redirect(url_for('main_blueprint.account', uname = uname))    
    
     
        