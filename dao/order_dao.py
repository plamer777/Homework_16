"""There's an OrderDao class in the unit. The class serves to return
orders by provided requests"""
from models.order_model import Order
from dao.user_dao import UserDao
# ------------------------------------------------------------------------
from utils import change_date_elements_order


class OrderDao(UserDao):
    """The OrderDao class was inherited from UserDao and have very similar
    logic. Only creat_dict method was changed to return correct dict"""
    @staticmethod
    def _create_dict(order: Order) -> dict:
        """The staticmethod to create a dict from an instance of Order class

        :param order: an instance of Order class

        return:
            single_order - a dict with order's data
        """
        single_order = {
            'id': order.id,
            'name': order.name,
            'description': order.description,
            'start_date': order.start_date,
            'end_date': order.end_date,
            'address': order.address,
            'price': order.price,
            'customer_id': order.customer_id,
            'executor_id': order.executor_id,
        }

        return single_order

    @staticmethod
    def _refresh_model(json_data: dict, order: Order) -> Order:
        """This is a closed method to update order's data in a model
        by provided json

        :param json_data: a dict with a data to update order's model
        :param order: a model to update data into

        :returns:
            order - an updated Order's class instance

        """

        order.id = json_data.get("id")
        order.name = json_data.get("name")
        order.description = json_data.get("description")
        order.start_date = json_data.get("start_date")
        order.end_date = json_data.get("end_date")
        order.address = json_data.get("address")
        order.price = json_data.get("price")
        order.customer_id = json_data.get("customer_id")
        order.executor_id = json_data.get("executor_id")

        return order

    def __repr__(self):

        return f"OrderDao({self.db}, {self.model})"
