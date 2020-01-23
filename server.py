# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

import re

app = Flask(__name__)
app.secret_key = '5ee400433891ad6cbbab41d7f18cf4ed734eefe44c9d85f230808704c49624cc7ab1b4b69488e18510f606194c970d8e6bdb510034fb5b92a6612001317490a9'
bcrypt = Bcrypt(app)

# Validation functions
def valid_email(email, flash_category):
    ret = True
    if len(email) == 0:
        flash(u'Cannot be blank', flash_category)
        ret = False
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if EMAIL_REGEX.match(email) == False:
        flash(u'Enter valid email', flash_category)
        ret = False
    return ret

def valid_name(name, flash_category):
    ret = True
    if len(name) == 0:
        flash(u'Cannot be blank', flash_category)
        ret = False
    elif len(name) < 3:
        flash(u'Must be more than two characters')
        ret = False

    VALID_NAME_REGEX = re.compile(r'[a-c]')
    if VALID_NAME_REGEX.match(name) == False:
        flash(u'Must be letters only', flash_category)
        ret = False
    else:
        return ret

def valid_new_password(password, password_confirmation):
    if len(password) >= 8:
        if password == password_confirmation:
            return True
        else:
            flash(u'Does not match', 'registration_password_confirmation')
    else:
        flash(u'Must be eight or more characters', 'registration_password_confirmation')
    return False

def valid_registration(form):
    ret = True
    if valid_name(form['first_name'], 'registration_first_name') == False:
        ret = False
    if valid_name(form['last_name'], 'registration_last_name') == False:
        ret = False
    if valid_email(form['email'], 'registration_email') == False:
        ret = False
    if valid_new_password(form['password'], form['password_confirmation'], 'registration_password') == False:
        ret = False
    return ret

# User functions
def authenticate_user(email, password):
    mysql = connectToMySQL("order_application")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = { 'email': request.form['email'] }
    users = mysql.query_db(query, data)
    if users:
        if bcrypt.check_password_hash(users[0]['password_hash'], password):
            session['user_id'] = users[0]['id']
            return True
    return False

def current_user():
    if session.get('user_id'):
        id = session.get('user_id')
        mysql = connectToMySQL("order_application")
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id': id }
        users = mysql.query_db(query, data)
        if users:
            return users[0]
    return False

def unauthorized():
    print('Unauthorized')
    flash(u'Unauthorized', 'main_warning')
    return redirect('/sessions/new')

# Root
@app.route('/')
def root():
    if current_user():
        return redirect('/orders')
    else:
        return redirect('/sessions/new')

# Sessions
@app.route('/sessions/create', methods = ['POST'])
def create_session():
    if authenticate_user(request.form['email'], request.form['password']) == True:
        return redirect('/orders')
    else:
        return unauthorized()

@app.route('/sessions/destroy', methods = ['DELETE', 'GET']) # GET to allow links
def destroy_session():
    session.clear()
    return redirect('/sessions/new')

@app.route('/sessions/new')
def new_session():
    return render_template('sessions/new.html')

# Users
@app.route('/users/create', methods = ['POST'])
def create_user():
    if valid_registration(request.form):
        password_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL("order_application")
        query = "INSERT INTO users (created_at, updated_at, email, first_name, last_name, password_hash) VALUES (NOW(), NOW(), %(email)s, %(first_name)s, %(last_name)s, %(password_hash)s);"
        data = { 'email': request.form['email'], 'password_hash': password_hash, 'first_name': request.form['first_name'], 'last_name': request.form['last_name'] }
        session['user_id'] = mysql.query_db(query, data)
        flash(u'Success! Your account is created.', 'main_info')
        return redirect('/orders')
    else:
        return redirect('/users/new')

@app.route('/users/new')
def new_user():
    return render_template('users/new.html')

if __name__ == '__main__':
    app.run(debug = True)