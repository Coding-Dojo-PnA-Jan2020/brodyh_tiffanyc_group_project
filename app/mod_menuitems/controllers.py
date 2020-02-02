from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, current_app
from app import db
from app.mod_menuitems.forms import MenuitemForm
from app.mod_menuitems.models import Menuitem
from app.mod_categories.models import Category
import os
from werkzeug.utils import secure_filename

mod_menuitems = Blueprint('menuitems', __name__, url_prefix = '/items')

def require_admin():
    if session.get('user_id'):
        from app.mod_users.models import User
        user = User.query.filter_by(id = session.get('user_id')).first()
        if not user == None:
            if not user.is_admin:
              return render_template('403.html'), 403
    else:
      return render_template('403.html'), 403

@mod_menuitems.route('/')
def index():
    menuitems = Menuitem.query.all()
    return render_template('menuitems/index.html', menuitems = menuitems)

@mod_menuitems.route('/appetizers')
def render_menu_appetizers():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('menuitems/menu-appetizers.html', menuitems = menuitems)

@mod_menuitems.route('/soups-salads')
def render_menu_soups_salads():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('menuitems/menu-soups-salads.html', menuitems = menuitems)

@mod_menuitems.route('/signature-dishes')
def render_menu_main_dishes():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('menuitems/menu-main-dishes.html', menuitems = menuitems)

@mod_menuitems.route('/desserts')
def render_menu_desserts():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('menuitems/menu-desserts.html', menuitems = menuitems)

@mod_menuitems.route('/drinks')
def render_menu_drinks():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('menuitems/menu-drinks.html', menuitems = menuitems)

@mod_menuitems.route('/new')
def new():
    require_admin()
    form = MenuitemForm(request.form)
    form.category.choices = [ (category.id, category.name) for category in Category.query.all() ]
    return render_template('menuitems/new.html', form = form)

@mod_menuitems.route('/create', methods = ['POST'])
def create():
    require_admin()
    form = MenuitemForm()
    form.category.choices = [ (category.id, category.name) for category in Category.query.all() ]
    if form.validate():
        category = Category.query.filter_by(id = int(form.category.data)).first()
        image = form.image.data
        image_file_path = os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], secure_filename(image.filename))
        image_url_path = f"uploads/{secure_filename(image.filename)}"
        image.save(image_file_path)
        menuitem = Menuitem(category, form.name.data, form.description.data, image_file_path, image_url_path, form.price.data)
        db.session.add(menuitem)
        db.session.commit()
        if menuitem:
            flash(f"Saved {menuitem.name}", 'main')
            return redirect(url_for('categories.show', name = category.name))
        else:
            flash('Database error', 'main')
    else:
        flash(form.errors, 'form_errors')
    return render_template('menuitems/new.html', form = form)