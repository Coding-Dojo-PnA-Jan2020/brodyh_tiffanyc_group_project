from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_sessions.forms import LoginForm
from app.mod_sessions.models import User

mod_sessions = Blueprint('sessions', __name__, url_prefix = '/sessions')

@mod_sessions.route('/new', methods = ['GET', 'POST'])
def new():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash(f'Welcome back {user.name}')
            return redirect(url_for('welcome.home'))
        flash('Wrong email or password', 'error-message')
    return render_template('sessions/signin.html', form = form)

@mod_sessions.route('/sessions/destroy', methods=['DELETE', 'GET'])
def destroy_session():
    session.clear()
    return redirect('/sessions/new')