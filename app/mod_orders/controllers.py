from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_orders.models import Order, OrderMenuitem
from app.mod_menuitems.models import Menuitem
from app.mod_payments.models import Payment
from app.mod_orders.forms import CartToOrderForm

mod_orders = Blueprint('orders', __name__, url_prefix = '/orders')

def current_user():
    if session.get('user_id'):
        from app.mod_users.models import User
        user = User.query.filter_by(id = session.get('user_id')).first()
        if not user == None:
            return user
    return None

@mod_orders.route('/create', methods = ['POST'])
def create():
    form = CartToOrderForm(request.form)
    user = current_user()
    if form.validate():
        if 'is_delivery' in request.form:
            is_delivery = True
        else:
            is_delivery = False

        payment = Payment(user.id, form.card_number.data)
        db.session.add(payment)
        db.session.commit()

        order = Order(user.id, payment.id, is_delivery, None, None, None, form.ready_by.data)
        db.session.add(order)
        db.session.commit()

        for menuitem_id in session['cart_menuitem_ids']:
            order_menuitem = OrderMenuitem(order.id, menuitem_id)
            db.session.add(order_menuitem)
            db.session.commit()

        if order:
          session['cart_menuitem_ids'] = []
          flash(f'Order placed')
          return redirect(url_for('orders.show', id = order.id))
        else:
          flash('Database error', 'main')
    else:
        flash(form.errors, 'form_errors')
    return render_template('cart/checkout.html', form = form)

@mod_orders.route('/<id>')
def show(id):
    order = Order.query.filter_by(id = id).first()
    payment = Payment.query.filter_by(id = order.payment_id)
    order_menuitems = OrderMenuitem.query.filter_by(order_id = id)

    menuitems = []
    for order_menuitem in order_menuitems:
        menuitems.append(Menuitem.query.filter_by(id = order_menuitem.menuitem_id))
    return render_template('orders/show.html', order = order, payment = payment, menuitems = menuitems)