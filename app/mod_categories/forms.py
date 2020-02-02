from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextField
from wtforms.validators import Required, EqualTo
from app import images

class CategoryForm(FlaskForm):
    name            = TextField('Name', [ Required(message = 'Please enter name') ])
    image           = FileField('Photo', validators = [FileRequired(), FileAllowed(images, 'Only images are accepted')])