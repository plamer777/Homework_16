"""The unit contains an Order class to work with a database"""
from sqlalchemy import ForeignKey
from source import db
# ------------------------------------------------------------------------


class Order(db.Model):
    """The Order class represents a logic to work with an order table
    in a database"""
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(250))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(250))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, ForeignKey('user.id'))
    customer = db.relationship('User', backref='order',
                               primaryjoin='Order.customer_id == User.id')
    executor = db.relationship('User',
                               primaryjoin='Order.executor_id == User.id')

    def __repr__(self):

        return f"Order({self.name}, {self.price})"
