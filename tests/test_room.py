import pytest

from sqlalchemy import text

@pytest.fixture(autouse=True)
def setup(db):
    db.execute(text("""
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
        """)
    )

@pytest.fixture(autouse=True)
def teardown(db):
    # Reset the id of rooms table to 1 after each test
    db.execute(text("ALTER TABLE rooms AUTO_INCREMENT = 1"))

    yield

    # Clean up rooms table after each test
    db.execute(text("SET FOREIGN_KEY_CHECKS=0"))
    db.execute(text("TRUNCATE rooms"))
    db.execute(text("SET FOREIGN_KEY_CHECKS=1"))

def test_create_room_with_closed_at(execute):
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
                "id": "5"
            }
        }
    }


def test_create_room_without_closed_at(execute):
    result = execute("""
        mutation {
            createRoom (
                roomInput : {
                    name: "new_room_1",
                    creatorId: 1,
                    storeId: 1
                }
            ) {
                id
            }
        }
    """)

    assert result == {
        "data": {
            "createRoom": {
                "id": "5"
            }
        }
    }

def test_get_room(execute):
    result = execute("""
        query {
            room(id: 3) {
                id,
                name,
                createdAt,
                closedAt,
                roomStatus {
                     id,
                     name
                },
                creator {
                     id,
                     slackName,
                     slackAccount,
                     profileImage,
                     slackCode
                },
                store {
                     id,
                     name,
                     yogiyoUrl
                }
            }
        }
    """)

    assert result == {
        "data": {
            "room": {
                "id": 3,
                "name": "햄벅햄벅",
                "createdAt": "2020-05-01T01:19:00",
                "closedAt": "2020-06-10T01:35:00",
                "roomStatus": {
                    "id": 2,
                    "name": "정산 중"
                },
                "creator": {
                    "id": 3,
                    "slackName": "정예진",
                    "slackAccount": "ohjtack@gmail.com",
                    "profileImage": "https://ca.slack-edge.com/TH0U6FBTN-UR3PU6YJE-1bcc2a09fc13-512",
                    "slackCode": "UR3PU6YJE"
                },
                "store": {
                    "id": 2,
                    "name": "참치의명가",
                    "yogiyoUrl": "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/372574/"
                },
            }
        }
    }

def test_get_rooms_status_2(execute):
    result = execute("""
        query {
            rooms(limit: 10, offset:0, status:2) {
                id,
                name,
                roomStatus {
                  id,
                  name
                },
                creator {
                  id,
                  slackName,
                  slackAccount,
                  profileImage,
                  slackCode
                },
                store {
                  id,
                  name,
                  yogiyoUrl
                },
                createdAt,
                closedAt
            }
        }
    """)

    assert result == {
        "data": {
            "rooms": [
                {
                    "id": 4,
                    "name": "초초초밥밥밥",
                    "roomStatus": {
                      "id": 2,
                      "name": "정산 중"
                    },
                    "creator": {
                      "id": 4,
                      "slackName": "홍수연",
                      "slackAccount": "ohjtack@gmail.com",
                      "profileImage": "http://img.kwangju.co.kr/upimages/gisaimg/00/02/37/00023791_P_0.jpg",
                      "slackCode": "UR3PU6YJE"
                    },
                    "store": {
                      "id": 2,
                      "name": "참치의명가",
                      "yogiyoUrl": "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/372574/"
                    },
                    "createdAt": "2020-04-01T01:20:00",
                    "closedAt": "2020-07-30T01:40:00"
                },
                {
                    "id": 3,
                    "name": "햄벅햄벅",
                    "roomStatus": {
                      "id": 2,
                      "name": "정산 중"
                    },
                    "creator": {
                      "id": 3,
                      "slackName": "정예진",
                      "slackAccount": "ohjtack@gmail.com",
                      "profileImage": "https://ca.slack-edge.com/TH0U6FBTN-UR3PU6YJE-1bcc2a09fc13-512",
                      "slackCode": "UR3PU6YJE"
                    },
                    "store": {
                      "id": 2,
                      "name": "참치의명가",
                      "yogiyoUrl": "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/372574/"
                    },
                    "createdAt": "2020-05-01T01:19:00",
                    "closedAt": "2020-06-10T01:35:00"
                }
            ]
        }
    }
