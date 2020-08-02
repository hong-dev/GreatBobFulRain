import pytest

from sqlalchemy import text

@pytest.fixture(autouse=True)
def setup_and_teardown(db):
    # Reset the id of rooms table to 1 after each test
    db.execute(text("ALTER TABLE rooms AUTO_INCREMENT = 1"))

    yield

    # Clean up rooms table after each test
    db.execute(text("SET FOREIGN_KEY_CHECKS=0"))
    db.execute(text("TRUNCATE rooms"))
    db.execute(text("SET FOREIGN_KEY_CHECKS=1"))

def test_create_room(execute):
    result = execute("""
        mutation {
            createRoom (
                roomInput : {
                    name: "new_room_1",
                    creatorId: 1,
                    storeId: 1,
                    closedAt: "2020-07-30T10:00:00"
                }
            ) {
                id
            }
        }
    """)

    assert result == {
        "data": {
            "createRoom": {
                "id": "1"
            }
        }
    }

