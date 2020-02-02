from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, current_app
from app import db
from app.mod_categories.forms import CategoryForm
from app.mod_categories.models import Category
from app.mod_menuitems.models import Menuitem
import os
from werkzeug.utils import secure_filename

mod_categories = Blueprint('categories', __name__, url_prefix = '/menu')

def require_admin():
    if session.get('user_id'):
        from app.mod_users.models import User
        user = User.query.filter_by(id = session.get('user_id')).first()
        if not user == None:
            if not user.is_admin:
              return render_template('403.html'), 403
    else:
      return render_template('403.html'), 403

@mod_categories.route('/')
def index():
    categories = Category.query.all()
    return render_template('categories/index.html', categories = categories)

@mod_categories.route('/new')
def new():
    require_admin()
    form = CategoryForm(request.form)
    return render_template('categories/new.html', form = form)

@mod_categories.route('/create', methods = ['POST'])
def create():
    require_admin()
    form = CategoryForm()
    if form.validate():
        image = form.image.data
        image_file_path = os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], secure_filename(image.filename))
        image_url_path = f"uploads/{secure_filename(image.filename)}"
        image.save(image_file_path)
        category = Category(form.name.data, image_file_path, image_url_path)
        db.session.add(category)
        db.session.commit()
        if category:
            flash(f"Saved {category.name}", 'main')
            return redirect(url_for('categories.index'))
        else:
            flash('Database error', 'main')
    else:
        flash(form.errors, 'form_errors')
    return render_template('categories/new.html', form = form)

@mod_categories.route('/<name>')
def show(name):
    category = Category.query.filter(Category.name.ilike(name)).first()
    menuitems = Menuitem.query.filter_by(category_id = category.id).all()
    return render_template('categories/show.html', category = category, menuitems = menuitems)