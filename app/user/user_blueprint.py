"""This file contains user blueprint and views to process requests about
users"""
from flask import Blueprint, jsonify, request
from dao.user_dao import UserDao
from models.user_model import User
from source import db
# ------------------------------------------------------------------------

# creating user's blueprint and UserDao instance
user_blueprint = Blueprint('user_blueprint', __name__)
user_dao = UserDao(db, User)


@user_blueprint.get('/users/')
def all_users_page():
    """This view returns json with all users' data found in database"""
    all_users = user_dao.get_all()

    return jsonify(all_users)


@user_blueprint.get('/users/<int:user_id>')
def single_user_page(user_id: int):
    """This view returns json with single user's data"""
    user = user_dao.get_one(user_id)

    return jsonify(user)


@user_blueprint.post('/users/')
def add_new_user():
    """This view adds a new user to database by a json received through request

    :returns:
        a string containing a result if adding was successful
    """
    new_user = request.json

    # if json data wasn't received then return appropriate message
    if not new_user:

        return "Не удалось получить данные"

    return user_dao.add_new(new_user)


@user_blueprint.put('/users/<int:user_id>')
def update_user_data(user_id: int):
    """This view updates user's data by a json received through request

    :param user_id: an id of the searched user

    :returns:
        a string containing a result if updating was successful
    """
    new_data = request.json

    if not new_data:

        return "Не удалось получить данные"

    return user_dao.update_data(user_id, new_data)


@user_blueprint.delete('/users/<int:user_id>')
def delete_user(user_id: int):
    """This view deletes user's data by provided user_id

    :param user_id: an id of the user to delete

    :returns:
        result - a string containing a result if operation was
        successful or not
    """
    result = user_dao.delete(user_id)

    return result
