from app.extensions import db
from datetime import datetime


class Order_item(db.Model):
    __tablename__ = "order_items"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    product_id = db.Column(db.Integer,db.ForeignKey("products.id"),nullable=False)
    product = db.relationship("Product",backref="order_items")
    price = db.Column(db.String(50),nullable=False)
    quantity = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)


    def __init__(self,product_id=None,price=None,quantity=None,**kwargs):
        super(Order_item, self).__init__(**kwargs)
        self.product_id=product_id
        self.price=price
        self.quantity=quantity