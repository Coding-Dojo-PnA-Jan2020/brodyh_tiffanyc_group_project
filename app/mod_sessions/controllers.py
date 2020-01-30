from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_sessions.forms import LoginForm
from app.mod_users.models import User

mod_sessions = Blueprint('sessions', __name__, url_prefix = '/sessions')

@mod_sessions.route('/new', methods = ['GET'])
def new():
    form = LoginForm(request.form)
    return render_template('sessions/new.html', form = form)

@mod_sessions.route('/create', methods = ['POST'])
def create():
    form = LoginForm(request.form)
    user = User.query.filter_by(email = form.email.data).first()
    if user and check_password_hash(user.password, form.password.data):
        session['user_id'] = user.id
        flash(f'Welcome back {user.first_name}!', 'main')
        if 'cart_menuitem_ids' in session:
            # Redirect to the checkout since the user probably just signed in after trying to checkout
            return redirect(url_for('cart.checkout'))
        else:
            return redirect(url_for('menuitems.index'))
    flash('Incorrect email or password', 'form_errors')
    return render_template('sessions/new.html', form = form)

@mod_sessions.route('/destroy', methods=['DELETE', 'GET'])
def destroy():
    session.clear()
    return redirect('/')