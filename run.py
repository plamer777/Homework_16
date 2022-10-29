"""This is a main file to run a Flask app"""
from source import app
from app.user.user_blueprint import user_blueprint
from app.order.order_blueprint import order_blueprint
from app.offer.offer_blueprint import offer_blueprint
# --------------------------------------------------------------------------

# blueprints' registration
app.register_blueprint(user_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(offer_blueprint)


@app.errorhandler(404)
def error_404(error):
    """This view returns a message if a route doesn't exist"""
    return f"К сожалению такая страница не найдена, код ошибки - {error}"


if __name__ == '__main__':

    app.run()
