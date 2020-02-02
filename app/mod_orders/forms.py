from flask_wtf import FlaskForm
from wtforms import BooleanField, DateTimeField, TextField
from wtforms.validators import Required, EqualTo

class CartToOrderForm(FlaskForm):
    name            = TextField('Name', [ Required(message = 'Please enter name') ])