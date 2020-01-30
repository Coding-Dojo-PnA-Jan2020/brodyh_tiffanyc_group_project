from app import db

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key = True)
    created_at    = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at    = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())

class Order(Base):
    __tablename__ = 'orders'

    user_id      = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    payment_id   = db.Column(db.Integer, db.ForeignKey('payments.id'), nullable = True) # Allow payments later
    is_delivery  = db.Column(db.Boolean, nullable = False)
    tax          = db.Column(db.Float, nullable = False)
    subtotal     = db.Column(db.Float, nullable = False)
    total        = db.Column(db.Float, nullable = False)
    ready_by     = db.Column(db.DateTime, nullable = False)

    def __init__(self, user_id, payment_id, is_delivery, tax, subtotal, total, ready_by):
        self.user_id     = user_id
        self.payment_id  = payment_id
        self.is_delivery = is_delivery
        self.tax         = tax
        self.subtotal    = subtotal
        self.total       = total
        self.ready_by    = ready_by

    def __repr__(self):
        return '<Order %r>' % (self.id)

class OrderMenuitem(Base):
    __tablename__ = 'order_menuitems'

    order_id    = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable = False)
    menuitem_id = db.Column(db.Integer, db.ForeignKey('menuitems.id'), nullable = False)

    def __init__(self, order_id, menuitem_id):
        self.order_id     = order_id
        self.menuitem_id  = menuitem_id

    def __repr__(self):
        return '<OrderMenuitem %r>' % (self.id)