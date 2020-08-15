from sqlalchemy import text

from .base_model import BaseModel

class Room(BaseModel):
    def __init__(
        self,
        id,
        name,
        created_at,
        closed_at,
        room_status_id,
        room_status_name,
        room_status_created_at,
        creator_id,
        store_id
    ):
        vars = locals()
        self.__dict__.update(vars)
        del self.__dict__["self"]

class RoomDao:
    def __init__(self, db):
        self.db = db

    def create_room(
        self,
        name       = None,
        closed_at  = None,
        creator_id = None,
        store_id   = None
    ):
        return self.db.execute(text("""
            INSERT INTO rooms (
                name,
                closed_at,
                creator_id,
                store_id
            ) VALUES (
                :name,
                :closed_at,
                :creator_id,
                :store_id
            )
        """), {
            'name'       : name,
            'closed_at'  : closed_at,
            'creator_id' : creator_id,
            'store_id'   : store_id
        }).lastrowid

    def get_room(self, id):
        room = self.db.execute(text("""
            SELECT
                rooms.id,
                rooms.name,
                rooms.created_at,
                rooms.closed_at,
                room_status.id as room_status_id,
                room_status.name as room_status_name,
                room_status.created_at as room_status_created_at,
                users.id as creator_id,
                stores.id as store_id
            FROM rooms

            JOIN room_status
            ON rooms.room_status_id = room_status.id
            JOIN users
            ON rooms.creator_id = users.id
            JOIN stores
            ON rooms.store_id = stores.id

            WHERE rooms.id = :id
        """), {"id" : id}).fetchone()

        return Room.from_row(room) if room else None

    def get_rooms(self, limit, offset, status):
        rooms = self.db.execute(text("""
            SELECT
                rooms.id,
                rooms.name,
                rooms.created_at,
                rooms.closed_at,
                room_status.id as room_status_id,
                room_status.name as room_status_name,
                room_status.created_at as room_status_created_at,
                users.id as creator_id,
                stores.id as store_id
            FROM rooms

            JOIN room_status
            ON rooms.room_status_id = room_status.id
            JOIN users
            ON rooms.creator_id = users.id
            JOIN stores
            ON rooms.store_id = stores.id

            WHERE room_status_id = :status

            ORDER BY
                CASE room_status_id
                    WHEN 1 THEN rooms.closed_at END ASC,
                CASE room_status_id
                    WHEN 2 THEN rooms.closed_at END DESC

            LIMIT  :limit
            OFFSET :offset
        """), {
            "limit"  : limit,
            "offset" : offset,
            "status" : status
        }).fetchall()

        return [ Room.from_row(room) for room in rooms ]
