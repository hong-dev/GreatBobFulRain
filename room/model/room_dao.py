from flask import jsonify
from mysql.connector.errors import Error

class RoomDao:

    """
    방 모델
    """

    def get_room_list(self, db_connection):
        """ 방 목록 표출

        Authors:
            jjuggumih@gmail.com

        History:
            2020-07-04 (jjuggumih@gmail.com): 초기 생성

        """

        try:
            with db_connection.cursor() as db_cursor:
                get_stmt = """
                    SELECT
                        name,
                        room_status_id,
                        creator_id,
                        store_id
                    FROM
                        rooms
                    ORDER BY
                        closed_at
                """

                db_cursor.execute(get_stmt)
                room_list = db_cursor.fetchall()
                if room_list:
                    return jsonify(room_list), 200
                return jsonify({'message': 'ROOM_DOES_NOT_EXIST'}), 404

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500
