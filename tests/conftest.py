import pytest
import config

from graphene.test import Client
from sqlalchemy    import create_engine

from api import schema, get_services

client   = Client(schema)
database = create_engine(config.TEST_DB_CONNECTION_URL)
services = get_services(database)

@pytest.fixture()
def execute():
    def _execute(query):
        return client.execute(query, context_value = services) 
    return _execute

@pytest.fixture()
def db():
    return database
