from flask import Flask, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_pages.controllers import mod_pages as pages_module
from app.mod_sessions.controllers import mod_sessions as sessions_module

app.register_blueprint(pages_module)
app.register_blueprint(sessions_module)

db.create_all()

@app.context_processor
def current_user():
    if session.get('user_id'):
        user = User.query.filter_by(id = session.get('user_id')).first()
        if user:
            print(dict(current_user = user))
            return dict(current_user = user)
    print(dict(current_user = None))
    return dict(current_user = None)