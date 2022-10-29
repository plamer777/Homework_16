"""This unit contains functions for testing purposes"""
from flask.testing import FlaskClient
# ------------------------------------------------------------------------


def check_all_records(records_list: list, keys: set) -> None:
    """The function checks a list of records

    :param records_list: a list of dicts
    :param keys: a set of keys to compare with records_list' keys
    """
    assert len(records_list) == 3, 'Список пуст'
    assert type(records_list) == list, 'В json лежит не список'

    for record in records_list:

        check_single_record(record, keys)


def check_single_record(record: dict, keys: set) -> None:
    """This function checks a single record

    :param record: a dict containing user, offer or order data
    :param keys: a set of keys to compare with record's keys
    """
    assert type(record) == dict, 'Тип данных в списке не верный'
    assert set(record) == keys, 'Ключи словаря неверные'


def check_received_data(testing_app: FlaskClient, route: str, test_json: dict):
    """This function checks a request received by provided route and keys
    with its values to compare them with test data

    :param testing_app: the testing application
    :param route: the testing route
    :param test_json: a dict with testing data
    """
    request = testing_app.get(f"{route}{test_json['id']}")

    received_json = request.json
    # creating a copy of test_json to avoid changing the original
    work_json = test_json.copy()

    assert request.status_code == 200, 'Статус код не ОК'
    assert set(received_json) == set(test_json), 'Ключи не совпадают'

    if 'start_date' in test_json:
        # changing dates info to None because of difference between formats
        remove_date(work_json, received_json)

    assert set(received_json.values()) == set(work_json.values()), \
        'Данные не совпадают'


def remove_date(received_json: dict, test_json: dict) -> None:
    """This function changes dates information to None

    :param received_json: a dict with received data
    :param test_json: a dict with test data to compare with received_json
    """
    for key in ('start_date', 'end_date'):
        received_json[key] = None
        test_json[key] = None
