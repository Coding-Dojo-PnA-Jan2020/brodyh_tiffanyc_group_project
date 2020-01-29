from app import db

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key = True)
    created_at    = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at    = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())

class Payment(Base):
    __tablename__ = 'payments'

    user_id      = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    card_number  = db.Column(db.Integer, nullable = True)

    def __init__(self, user_id, card_number):
        self.user_id     = user_id
        self.card_number = card_number

    def __repr__(self):
        return '<Payment %r>' % (self.id)