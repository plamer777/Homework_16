import pytest
from tests.configs.tests_config import USER_TEST_JSON, OFFER_TEST_JSON, \
    ORDER_TEST_JSON
from dao.db_dao import DatabaseDAO
from tests.source.tests_source import db, User, Order, Offer
from run import app
# -------------------------------------------------------------------------


@pytest.fixture()
def db_dao_testing():
    """This fixture serves to test DatabaseDAO class"""

    db_dao = DatabaseDAO(db)

    return db_dao


class TestDatabaseDAO:
    """The TestDatabaseDAO class provides a logic to test database creation
    methods of DatabaseDAO class"""

    def test_db_creation(self, db_dao_testing):
        """This method tests database creation methods of DatabaseDAO class

        :param db_dao_testing: a test fixture with DatabaseDAO's
        class instance
        """
        with app.app_context():

            # creation of database by using prepared models
            db.create_all()

            # filling up a database with models' data
            db_dao_testing.add_data_from_json(USER_TEST_JSON, User)
            db_dao_testing.add_data_from_json(ORDER_TEST_JSON, Order)
            db_dao_testing.add_data_from_json(OFFER_TEST_JSON, Offer)

            with db.session.begin():

                # receiving data from database to check out
                users = db.session.query(User).all()
                orders = db.session.query(Order).all()
                offers = db.session.query(Offer).all()

            assert len(users) == 3, 'Кол-во пользователей не верно'
            assert len(orders) == 3, 'Кол-во заказов не верно'
            assert len(offers) == 3, 'Кол-во предложений не верно'

            assert type(users[0]) is User, 'Класс модели пользователя не User'
            assert type(orders[0]) is Order, 'Класс модели заказа не Order'
            assert type(offers[0]) is Offer, 'Класс модели предложения ' \
                                             'не Offer'
