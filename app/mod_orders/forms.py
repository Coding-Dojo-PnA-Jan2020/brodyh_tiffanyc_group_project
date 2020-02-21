from flask_wtf import FlaskForm
from wtforms import BooleanField, DateTimeField, TextField
from wtforms.validators import Required, EqualTo

from datetime import datetime

class CartToOrderForm(FlaskForm):
    is_delivery    = BooleanField('Delivery?')
    ready_by       = DateTimeField('Ready By', [ Required(message = 'When would you like it by?') ], format = '%Y-%m-%dT%H:%M:%S', default = datetime.today)
    card_number    = TextField('Card #', [ Required(message = 'Please include your card number') ]) 