from flask import (
    request,
    jsonify,
    Blueprint
)

from room.service.room_service import RoomService
from connection import get_db_connection

class RoomView:
    room_app = Blueprint('room_app', __name__, url_prefix='/room')

    @room_app.route('', methods = ['GET'], endpoint='get_room_list')
    def get_room_list():
        try:
            db_connection = get_db_connection()
            if db_connection:
                room_service = RoomService()
                room_list = room_service.get_room_list(db_connection)
                return room_list

            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message': f'{e}'}), 500

        finally:
            try:
                db_connection.close()

            except Exception as e:
                return jsonify({'message': f'{e}'}), 500
