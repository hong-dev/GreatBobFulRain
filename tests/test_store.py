import pytest

from sqlalchemy import text

@pytest.fixture(autouse=True)
def setup_and_teardown(db):
    # Reset the id of stores table to 1 after each test
    db.execute(text("ALTER TABLE rooms AUTO_INCREMENT = 1"))

    yield

    # Clean up stores table after each test
    db.execute(text("SET FOREIGN_KEY_CHECKS=0"))
    db.execute(text("TRUNCATE rooms"))
    db.execute(text("SET FOREIGN_KEY_CHECKS=1"))

def test_get_store(execute):
    result = execute("""
        query {
            store(id: 2) {
                id,
                name,
                yogiyoUrl
            }
        }
    """)

    assert result == {
        "data": {
            "store": {
                "id": 2,
                "name": "참치의명가",
                "yogiyoUrl": "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/372574/"
            }
        }
    }

def test_get_stores(execute):
    result = execute("""
        query {
            stores(limit: 10, offset: 0) {
                id,
                name,
                yogiyoUrl
            }
        }
    """)

    assert result == {
        "data": {
            "stores": [
                {
                    "id": 1,
                    "name": "바스버거-선릉점",
                    "yogiyoUrl": "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/261890/"
                },
                {
                    "id": 2,
                    "name": "참치의명가",
                    "yogiyoUrl": "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/372574/"
                }
            ]
        }
    }

