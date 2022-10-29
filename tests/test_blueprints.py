"""This unit contains a TestBlueprints class to test all routes in a Flask
application"""
import pytest
from flask.testing import FlaskClient
from tests.source.tests_source import ROUTES_AND_KEYS, \
    ROUTE_AND_JSON_ADD, ROUTE_AND_JSON_UPDATE
from tests.testing_utils import check_all_records, check_single_record, \
    check_received_data
from run import app
# -------------------------------------------------------------------------


@pytest.fixture()
def testing_app():
    """This fixture provides a test client of the Flask application

    :returns:
        testing_client - a test client of the Flask application
    """
    testing_client = app.test_client()

    return testing_client


class TestBlueprints:
    """TestBlueprints class contains all necessary methods for testing
    purposes"""

    @pytest.mark.parametrize('route, keys', ROUTES_AND_KEYS)
    def test_all_page(self, testing_app: FlaskClient, route: str, keys: set):
        """This method tests receiving all records from provided routes

        :param testing_app: a test client of the Flask application
        :param route: current route to test
        :param keys: a set of keys to compare with keys in received json
        """
        request = testing_app.get(route)

        assert request.status_code == 200, 'Статус код не ОК'

        # this function serves to check many records at once
        check_all_records(request.json, keys)

    @pytest.mark.parametrize('route, keys', ROUTES_AND_KEYS)
    def test_single_page(self, testing_app: FlaskClient, route: str, keys):
        """This method tests receiving a single record from provided routes

        :param testing_app: a test client of the Flask application
        :param route: current route to test
        :param keys: a set of keys to compare with keys in received json
        """
        # testing a current route, I use 'id'=1 to get a record
        request = testing_app.get(f"{route}1")

        assert request.status_code == 200, 'Статус код не ОК'

        # checking a single record because there's only one dict in this
        # occasion
        check_single_record(request.json, keys)

    @pytest.mark.parametrize('route, test_json', ROUTE_AND_JSON_ADD)
    def test_add_new_page(self, testing_app, route, test_json):
        """This method tests post requests by provided routes

        :param testing_app: a test client of the Flask
        :param route: current route to test
        :param test_json: a dictionary with test data
        """
        request = testing_app.post(route, json=test_json)

        assert request.status_code == 200, 'Статус код не ОК'

        assert 'Данные добавлены успешно' in request.text, \
            'Данные не добавлены'

        # a comparison if added data is the same that test data
        check_received_data(testing_app, route, test_json)

    @pytest.mark.parametrize('route, test_json', ROUTE_AND_JSON_UPDATE)
    def test_update_page(self, testing_app: FlaskClient, route, test_json):
        """This method tests put requests by provided routes to update a
        record in the database

        :param testing_app: a test client of the Flask
        :param route: current route to test
        :param test_json: a dictionary with test data
        """
        request = testing_app.put(f"{route}{test_json['id']}", json=test_json)

        assert request.status_code == 200, 'Статус код не ОК'

        assert 'Данные обновлены успешно' in request.text, \
            'Данные не добавлены'

        # checking an updated data
        check_received_data(testing_app, route, test_json)

    @pytest.mark.parametrize('route, test_json', ROUTE_AND_JSON_UPDATE)
    def test_delete_page(self, testing_app: FlaskClient, route, test_json):
        """This method tests delete requests by provided routes

        :param testing_app: a test client of the Flask
        :param route: current route to test
        :param test_json: a dictionary with test data
        """

        # deleting a record that was updated on previous step
        request = testing_app.delete(f"{route}{test_json['id']}")

        assert request.status_code == 200, 'Статус код не ОК'
        assert request.text == f"Удаление записи с pk {test_json['id']} " \
                               f"прошло успешно", 'Ошибка при удалении'
        # checking if a record was deleted
        request = testing_app.get(f"{route}{test_json['id']}")

        assert request.status_code == 200, 'Статус код не ОК'
        assert "не найдена" in request.text, "Запись не удалена"
