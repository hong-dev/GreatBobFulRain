from flask      import Flask
from flask_cors import CORS

from pingpong.view.pingpong_view import PingPongView
def create_app():
    """
    """

    app = Flask(__name__)
    app.config['DEBUG'] = True
    CORS(app)

    app.register_blueprint(PingPongView.pingpong_app)

    return app
