"""
Create store table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
         CREATE TABLE stores (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(500) NOT NULL,
            yogiyo_url VARCHAR(2000) NULL,
            primary key(id)
         );
         """,
         ignore_errors='apply'),
    step("""
         INSERT INTO stores (id, name, yogiyo_url)
         VALUES (
            1,
            '바스버거-선릉점',
            'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/261890/'
        ),(
            2,
            '참치의명가',
            'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsYJgyr2N5xOVjj_oONYked4F3zAYpcOGoymnR8MJt_AU5b8YEkmNuBoCk3gQAvD_BwE#/372574/'
        );
        """,
        ignore_errors='apply')
]
