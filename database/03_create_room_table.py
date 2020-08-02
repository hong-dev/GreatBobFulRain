from yoyo import step

"""
Create room_status table
"""

__depends__ = {}

steps = [
    step(
        """
         CREATE TABLE room_status (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
            primary key(id)
        );
        """,
        ignore_errors="apply",
    ),
    step(
        """
         INSERT INTO room_status (id, name)
         VALUES (1, "주문 전"), (2, "정산 중")
        """,
        ignore_errors="apply",
    ),
]


"""
Create room table
"""

__depends__ = {'01_create_user_table', '02_create_store_table'}

steps = [
    step("""
         CREATE TABLE rooms (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(500) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            closed_at TIMESTAMP NULL,
            room_status_id INT NOT NULL DEFAULT 1,
            creator_id INT NOT NULL,
            store_id INT NOT NULL,
            primary key(id),
         CONSTRAINT room_status_id_fkey FOREIGN KEY (room_status_id) REFERENCES room_status(id),
         CONSTRAINT creator_id_fkey FOREIGN KEY (creator_id) REFERENCES users(id),
         CONSTRAINT store_id_fkey FOREIGN KEY (store_id) REFERENCES stores(id)
        );
        """,
        ignore_errors='apply'),
    step("""
         INSERT INTO rooms (
            `id`,
            `name`,
            `created_at`,
            `closed_at`,
            `room_status_id`,
            `creator_id`,
            `store_id`
         )
         VALUES (
            1,
            '바스버거 드실 분',
            '2020-06-15 01:19:00',
            '2020-06-30 01:35:00',
            1,
            1,
            1
         ),(
            2,
            '초밥 ㄱㄱ',
            '2020-06-20 01:20:00',
            '2020-06-25 01:40:00',
            1,
            2,
            2
         ),(
            3,
            '햄벅햄벅',
            '2020-05-01 01:19:00',
            '2020-06-10 01:35:00',
            2,
            3,
            2
         ),(
            4,
            '초초초밥밥밥',
            '2020-04-01 01:20:00',
            '2020-07-30 01:40:00',
            2,
            4,
            2
         );
         """,
         ignore_errors='apply')
]
