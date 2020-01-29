from flask_wtf import FlaskForm
from wtforms import BooleanField, DateTimeField, TextField
from wtforms.validators import Required, EqualTo

class CartToOrderForm(FlaskForm):
    is_delivery    = BooleanField('Delivery?', [ Required(message = 'Let us know if this is for delivery') ])
    ready_by       = DateTimeField('Ready By', [ Required(message = 'When would you like it by?') ])