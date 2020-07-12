"""
Create user_status table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(""" 
        CREATE TABLE user_status (
            id INT NOT NULL AUTO_INCREMENT,
            status VARCHAR(50) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
            primary key(id)
        );
    """, ignore_errors='apply'),
    step("""
         INSERT INTO user_status (id, status)
         VALUES (1, "PENDING"), (2, "SIGNED_UP")
    """, ignore_errors='apply')
]

