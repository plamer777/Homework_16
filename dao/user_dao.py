"""This unit contains Dao class to get necessary information from
a database."""
from flask_sqlalchemy import SQLAlchemy

from models.user_model import User
from utils import change_date_elements_order


class UserDao:
    """This class processes all requests and returns necessary data"""
    def __init__(self, db_obj: SQLAlchemy, model) -> None:
        """Initialization the class, saving database object and user model
        into class' fields

        :param db_obj: a database object
        :param model: a class describing a model
        """
        self.db = db_obj
        self.model = model

    def get_all(self) -> list:
        """This method returns a list of dicts with requested data

        return:
            all_users - a list of dicts
        """
        users = self.db.session.query(self.model).all()

        if users is None:

            return f"Не удалось получить данные о пользователях"

        all_users = []

        for user in users:

            single_user = self._create_dict(user)

            all_users.append(single_user)

        return all_users

    def get_one(self, user_id: int) -> dict:
        """This method returns a single user found by id

        :param user_id: the user's pk

        return:
            user - a dict with user's data
        """
        user = self.db.session.query(self.model).get(user_id)

        if user is not None:

            user = self._create_dict(user)
            return user

        return f"Запись с pk {user_id} не найдена"

    @staticmethod
    def _create_dict(user: User) -> dict:
        """The staticmethod to create a dict from an instance of User class

        :param user: an instance of User class

        :returns:
            single_user - a dict with user's data
        """
        single_user = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age,
            'email': user.email,
            'role': user.role,
            'phone': user.phone
        }

        return single_user

    def add_new(self, json_data: dict):
        """This method serves to add new data in a certain table

        :param json_data: a dict with data to add in table

        :returns:
            a string with result if adding was successful or not
        """
        work_json = json_data.copy()

        if {'start_date', 'end_date'}.issubset(set(json_data)):

            work_json = change_date_elements_order(json_data)

        try:
            with self.db.session.begin():

                # creation of new user by using json data
                new_user = self.model(**work_json)

                self.db.session.add(new_user)

            return f"Данные добавлены успешно: {new_user}"

        except Exception as e:

            return f"Не удалось выполнить запрос, возникла ошибка {e}"

    def update_data(self, pk: int, json_data: dict):
        """This method updates data in a certain table by provided 'pk' and
        dict with data

        :param pk: an id of searched record in the table
        :param json_data: a dict with a data to update

        :returns:
            a string with result if updating was successful or not
        """
        # if data keys are into json_data then to create python data strings
        # from those provided in json_data. This is used in child classes
        if {'start_date', 'end_date'}.issubset(set(json_data)):

            json_data = change_date_elements_order(json_data)

        # starting a new session
        with self.db.session.begin():
            user = self.db.session.query(self.model).get(pk)

            updated_user = self._refresh_model(json_data, user)

            try:
                # adding an updated user's data
                self.db.session.add(updated_user)

                return f"Данные обновлены успешно {updated_user}"

            except Exception as e:

                return f"В ходе обновления данных возникла ошибка {e}"

    @staticmethod
    def _refresh_model(json_data: dict, user: User):
        """This is a closed method to update user data in a model
        by provided json

        :param json_data: a dict with a data to update user's model
        :param user: a model to update data into

        :returns:
            user - an updated User's class instance

        """
        user.id = json_data.get("id")
        user.first_name = json_data.get("first_name")
        user.last_name = json_data.get("last_name")
        user.email = json_data.get("email")
        user.age = json_data.get("age")
        user.role = json_data.get("role")
        user.phone = json_data.get("phone")

        return user

    def delete(self, pk: int) -> str:
        """This method serves to a data from a table by provided 'pk'

        :param pk: an id of record to delete

        :returns:
            a string containing result of the operation
        """
        try:
            with self.db.session.begin():

                record = self.model.query.get(pk)

                if not record:

                    return "Нет такой записи в базе данных"

                self.db.session.delete(record)

            return f"Удаление записи с pk {pk} прошло успешно"

        except Exception as e:

            return f"При попытке удаления возникла ошибка {e}"

    def __repr__(self):

        return f"UserDao({self.db}, {self.model})"
