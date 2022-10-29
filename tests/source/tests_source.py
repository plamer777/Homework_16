"""This file provides data and objects for tests"""
from models.user_model import User
from models.order_model import Order
from models.offer_model import Offer
from source import db
from dao.user_dao import UserDao
from dao.offer_dao import OfferDao
from dao.order_dao import OrderDao
# ------------------------------------------------------------------------


# dicts to test if adding new object in a database works correctly
TEST_ADD_USER_JSON = {"id": 69,
                      "first_name": "John",
                      "last_name": "Dow",
                      "age": 58,
                      "email": "elliot16@mymail.com",
                      "role": "customer",
                      "phone": "6197021684"}

TEST_ADD_ORDER_JSON = {"id": 55,
                       "name": "Позвать в гости девушку",
                       "description":
                               "Позвать в гости девушку и шикануть перед "
                               "ней — заказать коробку конфет "
                               "с доставкой на дом",
                       "start_date": "01/24/2016",
                       "end_date": "03/10/2076",
                       "address": "9387 Grimes Green Apt. 801\nPagetown, "
                                  "NM 44165",
                       "price": 2800,
                       "customer_id": 18,
                       "executor_id": 25}

TEST_ADD_OFFER_JSON = {"id": 48,
                       "order_id": 35,
                       "executor_id": 4}
# -------------------------------------------------------------------------

# this dicts serves to check a work of updating function of DAOs
TEST_USER_JSON_UPDATE = {"id": 69,
                         "first_name": "Bread",
                         "last_name": "Pitt",
                         "age": 35,
                         "email": "elliot16@mymail.com",
                         "role": "customer",
                         "phone": "6197021684"}

TEST_ORDER_JSON_UPDATE = {"id": 55,
                          "name": "Позвать в гости девушку",
                          "description": "Позвать в гости девушку и "
                                         "шикануть перед "
                                         "ней — заказать коробку конфет "
                                         "с доставкой на дом",
                          "start_date": "01/24/2016",
                          "end_date": "03/10/2076",
                          "address": "9387 Grimes Green Apt. 801\n"
                                     "Pagetown, NM 44165",
                          "price": 5000,
                          "customer_id": 18,
                          "executor_id": 25}

TEST_OFFER_JSON_UPDATE = {"id": 48,
                          "order_id": 8,
                          "executor_id": 4}
# ------------------------------------------------------------------------

# test keys to compare with ones getting from the database
TEST_KEYS = [
    {'id',
     'first_name',
     'last_name',
     'email',
     'phone',
     'age',
     'role'},

    {'id',
     'name',
     'description',
     'start_date',
     'end_date',
     'address',
     'price',
     'customer_id',
     'executor_id'},

    {'id',
     'order_id',
     'executor_id'}
]
# ------------------------------------------------------------------------
# routes to test a Flask app
ROUTES = ['/users/', '/orders/', '/offers/']

# ------------------------------------------------------------------------

# creation DAOs' instances
user_dao = UserDao(db, User)
order_dao = OrderDao(db, Order)
offer_dao = OfferDao(db, Offer)
# ------------------------------------------------------------------------

# creation lists of objects to construct new lists to parameterize test
# methods
DAO_LIST = [user_dao, order_dao, offer_dao]
ADD_NEW_DATA_JSONS = [TEST_ADD_USER_JSON, TEST_ADD_ORDER_JSON,
                      TEST_ADD_OFFER_JSON]
UPDATE_DATA_JSONS = [TEST_USER_JSON_UPDATE, TEST_ORDER_JSON_UPDATE,
                     TEST_OFFER_JSON_UPDATE]
# ------------------------------------------------------------------------

# buildings new lists of objects to use for parameterizing test methods
DAO_KEYS_TESTING = [(test_dao, key) for test_dao, key in zip(
    DAO_LIST, TEST_KEYS)]

DAO_AND_JSON_ADD = [(test_dao, test_json) for test_dao, test_json in zip(
    DAO_LIST, ADD_NEW_DATA_JSONS)]

DAO_AND_JSON_UPDATE = [(test_dao, test_json) for test_dao, test_json in zip(
    DAO_LIST, UPDATE_DATA_JSONS)]

ROUTE_AND_JSON_ADD = [(route, test_json) for route, test_json in zip(
    ROUTES, ADD_NEW_DATA_JSONS)]

ROUTE_AND_JSON_UPDATE = [(route, test_json) for route, test_json in zip(
    ROUTES, UPDATE_DATA_JSONS)]

ROUTES_AND_KEYS = [(route, key) for route, key in zip(ROUTES, TEST_KEYS)]
