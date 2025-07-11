from app.extensions import db
from datetime import datetime


class Product(db.Model):
    __tablename__= "products"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    price = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text(),nullable=False)
    category = db.Column(db.String(100),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)


    def __init__(self,name=None, price=None, description=None, category=None, **kwargs):
        super(Product, self).__init__(**kwargs)
        self.name = name
        self.price = price
        self.description = description
        self.category = category