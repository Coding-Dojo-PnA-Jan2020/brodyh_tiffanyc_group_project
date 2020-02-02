from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SelectField, PasswordField, TextField
from wtforms.validators import Required, EqualTo
from app import images

class MenuitemForm(FlaskForm):
    name            = TextField('Name', [ Required(message = 'Please enter name') ])
    category        = SelectField('Category', [ Required(message = 'Please select a category') ], coerce = int)
#    category        = QuerySelectField('Category', query_factory = lambda: Category.query.all(), [ DataRequired() ])
    description     = TextField('Description', [ Required(message = 'Please enter description') ])
    price           = TextField('Price', [ Required(message = 'Enter a valid price') ])
    image           = FileField('Photo', validators = [FileRequired(), FileAllowed(images, 'Only images are accepted')])