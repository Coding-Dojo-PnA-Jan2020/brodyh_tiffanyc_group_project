from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_users.forms import RegistrationForm
from app.mod_users.models import User

mod_users = Blueprint('users', __name__, url_prefix = '/users')

@mod_users.route('/new')
def new():
    form = RegistrationForm()
    return render_template('users/new.html', form = form)

@mod_users.route('/create', methods = ['POST'])
def create():
    form = RegistrationForm()
    if form.validate():
        if form.password.data == form.password_confirmation.data:
            user = User(form.first_name.data, form.last_name.data, form.email.data, form.phone.data, generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            if user:
              session['user_id'] = user.id
              flash(f'Welcome back {user.first_name}!')
              return redirect(url_for('pages.about'))
            else:
              flash('Database error', 'main_warning')
        else:
            flash('Password and password confirmation do not match', 'form_errors')
    else:
        flash(form.errors, 'form_errors')

    return render_template('users/new.html', form = form)

@mod_users.route('/me')
def me():
    # current_user is already defined, so don't query User model
    return render_template('users/me.html')