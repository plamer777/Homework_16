"""The unit contains an OfferDao class to return offers by user's request"""
from dao.user_dao import UserDao
from models.offer_model import Offer
# -------------------------------------------------------------------------


class OfferDao(UserDao):
    """The OfferDao class was inherited from UserDao and have very similar
        logic. Only creat_dict method was changed to return a correct dict"""

    @staticmethod
    def _create_dict(offer: Offer) -> dict:
        """The staticmethod to create a dict from an instance of Offer class

        :param offer: an instance of Offer class

        return:
            single_offer - a dict with offer's data
        """
        single_offer = {
            'id': offer.id,
            'order_id': offer.order_id,
            'executor_id': offer.executor_id
        }

        return single_offer

    @staticmethod
    def _refresh_model(json_data: dict, offer: Offer) -> Offer:
        """This is a closed method to update offer's data in a model
        by provided json

        :param json_data: a dict with a data to update offer's model
        :param offer: a model to update data into

        :returns:
            offer - an updated Offer's class instance

        """
        offer.id = json_data.get("id")
        offer.order_id = json_data.get("order_id")
        offer.executor_id = json_data.get("executor_id")

        return offer

    def __repr__(self):

        return f"OfferDao({self.db}, {self.model})"
