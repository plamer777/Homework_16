"""This file contains views to process /offer requests"""
from flask import Blueprint, jsonify, request
from dao.offer_dao import OfferDao
from models.offer_model import Offer
from source import db
# --------------------------------------------------------------------------

# offer blueprint creation
offer_blueprint = Blueprint('offer_blueprint', __name__)
# creating an OfferDao instance
offer_dao = OfferDao(db, Offer)


@offer_blueprint.get('/offers/')
def all_offers_page():
    """This view returns json with all offers' data found in a database

    :returns:
        all_offers - a json with offers' data

    """
    all_offers = offer_dao.get_all()

    return jsonify(all_offers)


@offer_blueprint.get('/offers/<int:offer_id>')
def single_offer_page(offer_id):
    """This view returns json with single offer data found in a database

    :returns:
        single_offer - a json with single offer data
    """
    single_offer = offer_dao.get_one(offer_id)

    return jsonify(single_offer)


@offer_blueprint.post('/offers/')
def add_new_offer():
    """This view adds a new offer to a database by a json received through
    request

    :returns:
        a string containing a result if adding was successful
    """
    new_offer = request.json

    # if json data wasn't received then return appropriate message
    if not new_offer:

        return "Не удалось получить данные"

    return offer_dao.add_new(new_offer)


@offer_blueprint.put('/offers/<int:offer_id>')
def update_offer_data(offer_id: int):
    """This view updates offer's data by a json received through request

    :param offer_id: an id of the searched offer

    :returns:
        a string containing a result if updating was successful
    """
    new_data = request.json

    if not new_data:

        return "Не удалось получить данные"

    return offer_dao.update_data(offer_id, new_data)


@offer_blueprint.delete('/offers/<int:offer_id>')
def delete_offer(offer_id: int):
    """This view deletes offer's data by provided offer_id

    :param offer_id: an id of the order to delete

    :returns:
        result - a string containing a result if operation was
        successful or not
    """
    result = offer_dao.delete(offer_id)

    return result
