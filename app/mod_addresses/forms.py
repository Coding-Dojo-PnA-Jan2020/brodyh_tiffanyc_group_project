from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required

class AddressForm(FlaskForm):
    street                = TextField('Street', [ Required(message = 'Enter street') ])
    street2               = TextField('Street (continued)')
    city                  = TextField('City', [ Required(message = 'Enter city') ])
    state                 = TextField('State', [ Required(message = 'Enter state (abbreviated)') ])
    zip_code              = TextField('ZIP Code',  [ Required(message = 'Enter ZIP code') ])