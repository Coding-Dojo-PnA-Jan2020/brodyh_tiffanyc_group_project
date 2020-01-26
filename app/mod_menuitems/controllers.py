from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_menuitems.forms import MenuitemForm
from app.mod_menuitems.models import Menuitem

mod_menuitems = Blueprint('menuitems', __name__, url_prefix = '/menu')

@mod_menuitems.route('/<menuitem_id>')
def show():
    return render_template('menuitems/show.html')

@mod_menuitems.route('/')
def index():
    menuitems = db.session.query(Menuitem).all()
    return render_template('menuitems/index.html')