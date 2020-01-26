from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class MenuitemForm(FlaskForm):
    name            = TextField('First name', [ Required(message = 'Please enter name') ])
    description     = TextField('Last name', [ Required(message = 'Please enter description') ])
    price           = TextField('Email address', [ Email(), Required(message = 'Enter a valid price') ])