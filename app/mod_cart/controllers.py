from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.mod_menuitems.models import Menuitem

mod_cart = Blueprint('cart', __name__, url_prefix = '/cart')

@mod_cart.route('/')
def index():
    if 'cart_menuitem_ids' in session:
        menuitems = Menuitem.query.filter(Menuitem.id.in_(session['cart_menuitem_ids'])).all()
    else:
        menuitems = None
    return render_template('cart/index.html', menuitems = menuitems)

@mod_cart.route('/checkout')
def checkout():
    return render_template('cart/checkout.html')

@mod_cart.route('/add/?menuitem=<id>', methods = ['POST'])
def add_to_cart(id):
    if 'cart_menuitem_ids' not in session:
        session['cart_menuitem_ids'] = []

    cart_menuitem_ids = session['cart_menuitem_ids']
    cart_menuitem_ids.append(id)
    session['cart_menuitem_ids'] = cart_menuitem_ids

    # Todo: Redirect to category
    return redirect('/')

@mod_cart.route('/remove/?menuitem=<id>', methods = ['POST', 'DELETE'])
def remove_from_cart(id):
    # Todo: Check over this
    if 'cart_menuitem_ids' not in session:
        session['cart_menuitem_ids'] = []
        cart_menuitem_ids = session['cart_menuitem_ids']
    else:
        cart_menuitem_ids = session['cart_menuitem_ids']
        cart_menuitem_ids.remove(id)

    return redirect(url_for('cart.index'))