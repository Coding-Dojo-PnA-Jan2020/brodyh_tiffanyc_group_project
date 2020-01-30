from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.mod_menuitems.models import Menuitem
from app.mod_orders.forms import CartToOrderForm
from app.mod_orders.models import Order, OrderMenuitem

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
    if 'user_id' in session:
        if 'cart_menuitem_ids' in session:
            if not session['cart_menuitem_ids'] == []:
                menuitems = Menuitem.query.filter(Menuitem.id.in_(session['cart_menuitem_ids'])).all()
                form = CartToOrderForm(request.form)
                return render_template('cart/checkout.html', menuitems = menuitems, form = form)
        flash('Please add menu items to the cart before checking out', 'main')
        return redirect(url_for('cart.index'))
    flash('Please sign in before checking out', 'main')
    return redirect(url_for('sessions.new'))

@mod_cart.route('/add/?menuitem=<id>', methods = ['POST'])
def add(id):
    if 'cart_menuitem_ids' not in session:
        session['cart_menuitem_ids'] = []

    cart_menuitem_ids = session['cart_menuitem_ids']
    cart_menuitem_ids.append(id)
    session['cart_menuitem_ids'] = cart_menuitem_ids
    print(session['cart_menuitem_ids'])

    flash('Added to cart', 'main')
    # Todo: Redirect to category
    return redirect(url_for('menuitems.index'))

@mod_cart.route('/remove/?menuitem=<id>', methods = ['POST', 'DELETE'])
def remove(id):
    if 'cart_menuitem_ids' not in session:
        session['cart_menuitem_ids'] = []
        cart_menuitem_ids = session['cart_menuitem_ids']
    else:
        cart_menuitem_ids = session['cart_menuitem_ids']
        cart_menuitem_ids.remove(id)
    flash('Removed from cart', 'main')
    return redirect(url_for('cart.index'))