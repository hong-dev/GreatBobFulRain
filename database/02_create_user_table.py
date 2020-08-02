"""
Create user table
"""

from yoyo import step

__depends__ = {'01_create_user_status_table'}

steps = [
    step("""
         CREATE TABLE users (
            id INT NOT NULL AUTO_INCREMENT,
            slack_name VARCHAR(100) NOT NULL,
            slack_account VARCHAR(100) NOT NULL,
            slack_code VARCHAR(100) NOT NULL,
            profile_image VARCHAR(2000),
            user_status_id INT NOT NULL DEFAULT 1,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            primary key(id),
            CONSTRAINT user_status_id_fkey FOREIGN KEY (user_status_id) REFERENCES user_status(id)
        );
    """, ignore_errors='apply'),
    step("""
         INSERT INTO users (
            id, slack_name, slack_account, slack_code, profile_image, created_at)
         VALUES (
            1,
            '오종택',
            'ohjtack@gmail.com',
            'UR3PU6YJE',
            'https://ca.slack-edge.com/TH0U6FBTN-UR3PU6YJE-1bcc2a09fc13-512',
            '2020-06-29 00:27:00'
        ),(
            2,
            '이소헌',
            'shlee',
            'UR3PU6YJE',
            'https://ca.slack-edge.com/TH0U6FBTN-UR3PU6YJE-1bcc2a09fc13-512',
            '2020-06-29 00:28:00'
        ),(
            3,
            '정예진',
            'ohjtack@gmail.com',
            'UR3PU6YJE',
            'https://ca.slack-edge.com/TH0U6FBTN-UR3PU6YJE-1bcc2a09fc13-512',
            '2020-06-29 00:29:00'
        ),(
            4,
            '홍수연',
            'ohjtack@gmail.com',
            'UR3PU6YJE',
            'http://img.kwangju.co.kr/upimages/gisaimg/00/02/37/00023791_P_0.jpg',
            '2020-06-29 00:30:00'
        );
    """, ignore_errors='apply')
]
