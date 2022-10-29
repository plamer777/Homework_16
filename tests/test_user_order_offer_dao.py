"""This unit serves to test three DAOs at once"""
import pytest
from tests.source.tests_source import DAO_KEYS_TESTING, \
    DAO_AND_JSON_ADD, DAO_AND_JSON_UPDATE
from tests.testing_utils import check_all_records, check_single_record, \
    remove_date
from run import app
# -------------------------------------------------------------------------


class TestDao:
    """The TestDao class provides methods to test User, Order and
    Offer DAOs"""

    @pytest.mark.parametrize('test_dao, keys', DAO_KEYS_TESTING)
    def test_get_all(self, test_dao, keys):
        """This method test get_all method of all three DAOs

        :param test_dao: one of the DAOs getting from DAO_KEYS_TESTING
        :param keys: a set of keys to compare against the ones getting from
        the database
        """
        with app.app_context():

            all_records = test_dao.get_all()

            # this function described in testing_utils module
            check_all_records(all_records, keys)

    @pytest.mark.parametrize('test_dao, keys', DAO_KEYS_TESTING)
    def test_get_one(self, test_dao, keys):
        """This method test get_one method of current DAO

        :param test_dao: one of the DAOs
        :param keys: a set of keys
        """
        with app.app_context():

            record = test_dao.get_one(1)

            # the function described in testing_utils module too
            check_single_record(record, keys)

    @pytest.mark.parametrize('test_dao, test_json_data', DAO_AND_JSON_ADD)
    def test_add_new(self, test_dao, test_json_data):
        """The method test add_new method of current DAO

        :param test_dao: one of the DAOs
        :param test_json_data: a dict with data to add in the database
        """
        with app.app_context():

            # checking adding result and if receiving added record from the
            # database
            result = test_dao.add_new(test_json_data)
            added_data = test_dao.get_one(test_json_data['id'])

        assert 'Данные добавлены успешно' in result, 'Данные не добавлены'

        assert set(added_data) == set(test_json_data), 'Ключи не совпадают'

        remove_date(added_data, test_json_data)

        assert set(added_data.values()) == set(test_json_data.values()), \
            'Значения не совпадают'

    @pytest.mark.parametrize('test_dao, test_json_data', DAO_AND_JSON_UPDATE)
    def test_update(self, test_dao, test_json_data):
        """The method serves to test update_data method used in all three
        DAOs

        :param test_dao: one of the DAOs
        :param test_json_data: a dict to update data in the database
        """
        with app.app_context():

            result = test_dao.update_data(test_json_data['id'], test_json_data)
            updated_data = test_dao.get_one(test_json_data['id'])

        assert 'Данные обновлены успешно' in result, 'Данные не обновились'
        assert set(updated_data) == set(test_json_data), 'Ключи не совпадают'

        # the function sets up None value for start_date and end_date keys
        # because of very different format between json ana the database
        remove_date(updated_data, test_json_data)

        assert set(updated_data.values()) == set(test_json_data.values()), \
            'Значения не совпадают'

    @pytest.mark.parametrize('test_dao, test_json_data', DAO_AND_JSON_UPDATE)
    def test_delete(self, test_dao, test_json_data):
        """This method tests if delete method of all DAOs works correctly

        :param test_dao: one of the DAOs
        :param test_json_data: a dict to get 'id' to delete certain record
        from the database
        """
        with app.app_context():

            result = test_dao.delete(test_json_data['id'])
            deleting_result = test_dao.get_one(test_json_data['id'])

        assert 'прошло успешно' in result, 'Данные не обновились'

        assert deleting_result == f"Запись с pk {test_json_data['id']} " \
                                  "не найдена", 'Запись не удалена'
