from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_orders.models import Order
from app.mod_payments.models import Payment

mod_payments = Blueprint('payments', __name__, url_prefix = '/payments')