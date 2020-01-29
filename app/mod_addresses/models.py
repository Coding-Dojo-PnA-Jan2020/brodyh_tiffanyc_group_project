from app import db

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key = True)
    created_at    = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at    = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())

class Address(Base):
    __tablename__ = 'addresses'

    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    street     = db.Column(db.String(128), nullable = False)
    street2    = db.Column(db.String(128), nullable = True)
    city       = db.Column(db.String(64), nullable = False)
    state      = db.Column(db.String(2), nullable = False)
    zip_code   = db.Column(db.Integer, nullable = False)

    def __init__(self, user_id, street, street2, city, state, zip_code):
        self.user_id  = user_id
        self.street   = street
        self.street2  = street2
        self.city     = city
        self.state    = state
        self.zip_code = zip_code

    def __repr__(self):
        return '<Address %r>' % (self.id)