from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class RegistrationForm(FlaskForm):
    first_name            = TextField('First name', [ Required(message = 'Please enter first name') ])
    last_name             = TextField('Last name', [ Required(message = 'Please enter your last name') ])
    email                 = TextField('Email address', [ Email(), Required(message = 'Forgot your email address?') ])
    phone                 = TextField('Phone number', [ Required(message = 'Forgot phone number?') ])
    password              = PasswordField('Password',  [ Required(message = 'Password is required') ])
    password_confirmation = PasswordField('Password confirmation',  [ Required(message = 'Please confirm your new password') ])