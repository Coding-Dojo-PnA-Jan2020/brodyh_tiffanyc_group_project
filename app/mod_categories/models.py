from app import db

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key = True)
    created_at    = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_at    = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())

class Category(Base):
    __tablename__ = 'categories'

    name            = db.Column(db.String(128), nullable = False)
    image_file_path = db.Column(db.String(128), nullable = False)
    image_url_path  = db.Column(db.String(128), nullable = False)

    def __init__(self, name, image_file_path, image_url_path):
        self.name            = name
        self.image_file_path = image_file_path
        self.image_url_path  = image_url_path

    def __repr__(self):
        return '<Category %r>' % (self.id)