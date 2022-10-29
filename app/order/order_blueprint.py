"""This unit contains blueprint to get orders by user's request"""
from flask import Blueprint, jsonify, request
from dao.order_dao import OrderDao
from source import db
from models.order_model import Order
# ------------------------------------------------------------------------

# blueprint's creation
order_blueprint = Blueprint('order_blueprint', __name__)
# creation an OrderDao instance
order_dao = OrderDao(db, Order)


@order_blueprint.get('/orders/')
def all_orders_page():
    """This view returns a list of all orders found in a database

    return:
        all_orders - json string with orders' data
    """
    all_orders = order_dao.get_all()

    return jsonify(all_orders)


@order_blueprint.get('/orders/<int:order_id>')
def single_order_page(order_id):
    """This view returns a single order found by its id

    :param order_id: an id of a searched order

    return:
        single_order - json string with single order's data
    """
    single_order = order_dao.get_one(order_id)

    return jsonify(single_order)


@order_blueprint.post('/orders/')
def add_new_order():
    """This view adds a new order to a database by a json received through
    request

    :returns:
        a string containing a result if adding was successful
    """
    new_order = request.json

    # if json data wasn't received then return appropriate message
    if not new_order:

        return "Не удалось получить данные"

    return order_dao.add_new(new_order)


@order_blueprint.put('/orders/<int:order_id>')
def update_order_data(order_id: int):
    """This view updates order's data by a json received through request

    :param order_id: an id of the searched order

    :returns:
        a string containing a result if updating was successful
    """
    new_data = request.json

    if not new_data:

        return "Не удалось получить данные"

    return order_dao.update_data(order_id, new_data)


@order_blueprint.delete('/orders/<int:order_id>')
def delete_order(order_id: int):
    """This view deletes order's data by provided order_id

    :param order_id: an id of the order to delete

    :returns:
        result - a string containing a result if operation was
        successful or not
    """
    result = order_dao.delete(order_id)

    return result
