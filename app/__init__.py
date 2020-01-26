from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_sessions.controllers import mod_sessions as sessions_module
app.register_blueprint(sessions_module)

db.create_all()