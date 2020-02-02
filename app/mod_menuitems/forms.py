from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo
from app import images

class MenuitemForm(FlaskForm):
    name            = TextField('Name', [ Required(message = 'Please enter name') ])
    description     = TextField('Description', [ Required(message = 'Please enter description') ])
    price           = TextField('Price', [ Required(message = 'Enter a valid price') ])
    image           = FileField('Photo', validators = [FileRequired(), FileAllowed(images, 'Only images are accepted')])