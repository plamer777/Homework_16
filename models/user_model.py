"""This file contains a User class is a model to work with a database"""
from source import db


class User(db.Model):
    """This class represents a User model to work with a database"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role = db.Column(db.String(15))
    phone = db.Column(db.String(30))

    def __repr__(self):

        return f"User({self.first_name}, {self.last_name})"
