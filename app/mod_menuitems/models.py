from app import db
from sqlalchemy.orm import relationship

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key = True)
    created_at    = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at    = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())

class Menuitem(Base):
    __tablename__ = 'menuitems'

    category_id     = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable = False)
    category        = relationship('Category', back_populates = 'menuitems')
    name            = db.Column(db.String(128), nullable = False)
    description     = db.Column(db.String(128), nullable = False)
    price           = db.Column(db.Float(), nullable = False)
    image_file_path = db.Column(db.String(128), nullable = False)
    image_url_path  = db.Column(db.String(128), nullable = False)

    def __init__(self, category, name, description, image_file_path, image_url_path, price):
        self.category        = category
        self.name            = name
        self.description     = description
        self.image_file_path = image_file_path
        self.image_url_path  = image_url_path
        self.price           = price

    def __repr__(self):
        return '<Menuitem %r>' % (self.name)