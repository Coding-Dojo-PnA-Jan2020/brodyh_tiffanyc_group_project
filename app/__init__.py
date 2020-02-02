from flask import Flask, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_addresses.controllers import mod_addresses as addresses_module
from app.mod_categories.controllers import mod_categories as categories_module
from app.mod_cart.controllers import mod_cart as cart_module
from app.mod_pages.controllers import mod_pages as pages_module
from app.mod_menuitems.controllers import mod_menuitems as menuitems_module
from app.mod_sessions.controllers import mod_sessions as sessions_module
from app.mod_orders.controllers import mod_orders as orders_module
from app.mod_payments.controllers import mod_payments as payments_module
from app.mod_users.controllers import mod_users as users_module

app.register_blueprint(addresses_module)
app.register_blueprint(cart_module)
app.register_blueprint(categories_module)
app.register_blueprint(pages_module)
app.register_blueprint(menuitems_module)
app.register_blueprint(orders_module)
app.register_blueprint(payments_module)
app.register_blueprint(sessions_module)
app.register_blueprint(users_module)

db.create_all()

@app.context_processor
def current_user():
    if session.get('user_id'):
        from app.mod_users.models import User
        user = User.query.filter_by(id = session.get('user_id')).first()
        if not user == None:
            return dict(current_user = user)
    return dict(current_user = None)

@app.context_processor
def cart_menuitem_ids():
    if 'cart_menuitem_ids' not in session:
        session['cart_menuitem_ids'] = []
    return dict(cart_menuitem_ids = session['cart_menuitem_ids'])