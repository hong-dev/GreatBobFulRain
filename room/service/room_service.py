from room.model.room_dao import RoomDao

class RoomService:
    def get_room_list(self, db_connection):
        room_dao = RoomDao()
        room_list = room_dao.get_room_list(db_connection)

        return room_list
