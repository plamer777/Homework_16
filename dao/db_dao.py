"""The file contains DatabaseDAO class to fill up the database from json
data"""
from flask_sqlalchemy import SQLAlchemy
from utils import load_from_json_file, change_date_elements_order
# --------------------------------------------------------------------------


class DatabaseDAO:
    """The DatabaseDAO class serves to fill up the database from json file"""

    def __init__(self, db_obj: SQLAlchemy):
        """Initialization method for DatabaseDAO that store
        a database object

        :param db_obj: the database object
        """
        self.db = db_obj

    def add_data_from_json(self, filename: str, model):
        """This method fills up a database from certain json file. There's
        a logic to fix a problem with data string loaded from json file.

        :param filename: the name of the json file
        :param model: the class to work with table from the database
        """
        # loading data from json file
        json_data = load_from_json_file(filename)

        models_list = []

        try:
            for record in json_data:
                # processing date string and fixing problem with data order
                if 'start_date' in record or 'end_date' in record:

                    record = change_date_elements_order(record)

                # creating a list of models to add in the database
                models_list.append(model(**record))

        except Exception as e:

            print(f'Не удалось создать модель на основе записи {record}, '
                  f'возникла ошибка {e}')

        if not models_list:

            print('Ни одной модели создать не удалось')
            return

        # adding data in the database
        self.db.session.add_all(models_list)
        self.db.session.commit()
        self.db.session.close()

    def __repr__(self):

        return f"DatabaseDAO({self.db})"
