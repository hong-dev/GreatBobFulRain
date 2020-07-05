from flask                       import Flask
from flask_cors                  import CORS
from flask_graphql               import GraphQLView

from pingpong.view.pingpong_view import PingPongView
from room.view.room_view         import RoomView

def create_app():
    """
    """

    app = Flask(__name__)
    app.config['DEBUG'] = True
    CORS(app)

    app.register_blueprint(PingPongView.pingpong_app)
    app.register_blueprint(RoomView.room_app)

    return app
