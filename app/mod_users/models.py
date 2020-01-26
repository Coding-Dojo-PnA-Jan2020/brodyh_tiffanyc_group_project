from app import db

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key = True)
    created_at    = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at    = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())

class User(Base):
    __tablename__ = 'users'

    first_name = db.Column(db.String(128), nullable = False)
    last_name  = db.Column(db.String(128), nullable = False)
    email      = db.Column(db.String(128), nullable = False)
    phone      = db.Column(db.String(128), nullable = False, unique = True)
    password   = db.Column(db.String(192), nullable = False)

    def __init__(self, first_name, last_name, email, phone, password):
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email
        self.phone      = phone
        self.password   = password

    def __repr__(self):
        return '<User %r>' % (self.first_name)