from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo

class MenuitemForm(FlaskForm):
    name            = TextField('Name', [ Required(message = 'Please enter name') ])
    description     = TextField('Description', [ Required(message = 'Please enter description') ])
    price           = TextField('Price', [ Required(message = 'Enter a valid price') ])