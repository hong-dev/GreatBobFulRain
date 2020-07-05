import pymysql

from config import DATABASES

def get_db_connection():

    """ 데이터베이스 커넥션 생성

    import 되어서 사용될 때마다 하나의 데이터베이스 커넥션이 생성

    Returns:
        database connection 객체

    Authors:
        jjuggumih@gmail.com

    History:
        2020-07-04 (jjuggumih@gmail.com): 초기 생성

    """
    db_config = {
        'database'   : DATABASES['database'],
        'user'       : DATABASES['user'],
        'password'   : DATABASES['password'],
        'host'       : DATABASES['host'],
        'port'       : DATABASES['port'],
        'charset'    : DATABASES['charset'],
        'cursorclass': pymysql.cursors.DictCursor,
    }
    db = pymysql.connect(**db_config)
    return db
