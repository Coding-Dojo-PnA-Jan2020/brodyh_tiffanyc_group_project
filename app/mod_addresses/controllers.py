from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_addresses.forms import AddressForm
from app.mod_addresses.models import Address

mod_addresses = Blueprint('addresses', __name__, url_prefix = '/addresses')