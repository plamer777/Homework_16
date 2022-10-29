"""This unit is used to load json data from a file"""
import json
from datetime import date
# --------------------------------------------------------------------------


def load_from_json_file(file_path: str):
    """This function loads data from a json file
    :param file_path: path to json file

    return:
        json_data - a python dictionary or list with data

    """
    try:
        with open(file_path, encoding='utf-8') as fin:

            json_data = json.load(fin)

        return json_data

    except Exception as e:

        print(f"При загрузке данных из файла возникла ошибка {e}")
        return []


def change_date_elements_order(record: dict) -> dict:
    """
    splitting date string by '/' symbol and creating a new
    appropriate date string

    :param record: a dictionary containing date information

    :returns:
        record - a dictionary with date in python format
    """
    work_record = record.copy()
    for key in ('start_date', 'end_date'):

        if work_record[key] is None:
            break

        # splitting date string by '/' symbol and changing an order of a date
        # parts
        fixed_date = record[key].split('/')
        fixed_date = '-'.join([fixed_date[2], fixed_date[0],
                               fixed_date[1]])

        # writing new date strings
        work_record[key] = date.fromisoformat(fixed_date)

    return work_record
