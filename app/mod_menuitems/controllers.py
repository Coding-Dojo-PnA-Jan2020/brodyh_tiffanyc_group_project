from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.mod_menuitems.forms import MenuitemForm
from app.mod_menuitems.models import Menuitem

mod_menuitems = Blueprint('menuitems', __name__, url_prefix = '/menu')

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

@mod_menuitems.route('/menu/appetizers')
def render_menu_appetizers():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('pages/menu-appetizers.html', menuitems = menuitems)

@mod_menuitems.route('/menu/soups-salads')
def render_menu_soups_salads():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('pages/menu-soups-salads.html', menuitems = menuitems)

@mod_menuitems.route('/menu/signature-dishes')
def render_menu_main_dishes():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('pages/menu-main-dishes.html', menuitems = menuitems)

@mod_menuitems.route('/menu/desserts')
def render_menu_desserts():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('pages/menu-desserts.html', menuitems = menuitems)

@mod_menuitems.route('/menu/drinks')
def render_menu_drinks():
    # Todo: Select menuitems belonging to category
    menuitems = Menuitem.query.all()
    return render_template('pages/menu-drinks.html', menuitems = menuitems)

@mod_menuitems.route('/new')
def new():
    require_admin()
    form = MenuitemForm(request.form)
    return render_template('menuitems/new.html', form = form)

@mod_menuitems.route('/create', methods = ['POST'])
def create():
    require_admin()
    form = MenuitemForm(request.form)
    if form.validate():
        menuitem = Menuitem(form.name.data, form.description.data, form.price.data)
        db.session.add(menuitem)
        db.session.commit()
        if menuitem:
          flash(f"Saved {menuitem.name}", 'main')
          return redirect(url_for('menuitems.index'))
        else:
          flash('Database error', 'main')
    else:
        flash(form.errors, 'form_errors')
    return render_template('menuitems/new.html', form = form)