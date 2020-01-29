from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_orders.models import Order, OrderMenuitem
from app.mod_payments.models import Payment

mod_orders = Blueprint('orders', __name__, url_prefix = '/orders')

@mod_orders.route('/create', methods = ['POST'])
def create():
    pass