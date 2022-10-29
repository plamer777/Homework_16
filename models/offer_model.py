"""There is an Offer class that is a model to work with offer table
in a database in the file"""
from sqlalchemy import ForeignKey

from source import db


class Offer(db.Model):
    """The Offer class is a model to work with offer table in a database"""
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, ForeignKey('user.id'))
    order = db.relationship('Order', backref='offer')
    executor = db.relationship('User', backref='offer')

    def __repr__(self):

        return f"Offer({self.id}, {self.order}, {self.executor})"
