class RoomService:
    def __init__(self, room_dao):
        self.room_dao = room_dao

    def get_room(self, id):
        return self.room_dao.get_room(id)

    def get_rooms(self, limit, offset, status):
        return self.room_dao.get_rooms(limit, offset, status)
