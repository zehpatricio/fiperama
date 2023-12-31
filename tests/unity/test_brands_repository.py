from unittest.mock import MagicMock
from dataclasses import asdict

import pytest
import pymongo

from app.core.models import Brand
from app.repository import BrandsRepository


@pytest.fixture
def mock_mongo_client():
    client = MagicMock(spec=pymongo.MongoClient)
    return client


@pytest.fixture(autouse=True)
def mock_mongo_connection(monkeypatch, mock_mongo_client):
    def mock_connection(*args, **kwargs):
        return mock_mongo_client

    monkeypatch.setattr(pymongo, "MongoClient", mock_connection)


@pytest.fixture
def repository():

    repo = BrandsRepository(
        "mongodb://localhost:27017/",
        "test_cars_db",
        "test_cars_collection"
    )

    return repo


@pytest.fixture
def mock_mongo_collection(mock_mongo_client):
    return mock_mongo_client["test_cars_db"]["test_cars_collection"]


def test_insert(repository, mock_mongo_collection):
    data = Brand(
        code='1',
        name='Brand',
        cars=[{
            'code': 1,
            'model': 'Test Model',
            'notes': 'Test Notes',
        }]
    )

    repository.insert(data)
    mock_mongo_collection.insert_one.assert_called_with(asdict(data))


def test_find(repository, mock_mongo_collection):
    query = {'code': '1'}
    
    repository.find(query)
    mock_mongo_collection.find.assert_called_with(query)


def test_update(repository, mock_mongo_collection):
    initial_data = Brand(
        code='1',
        name='Brand',
        cars=[{
            'code': 2,
            'model': 'Initial Model',
            'notes': 'Initial Notes',
        }]
    )
    repository.insert(initial_data)

    filter_query = {'code': 2}
    update_data = {'$set': {'model': 'Updated Model'}}
    repository.update(filter_query, update_data)

    mock_mongo_collection.update_many.assert_called_with(
        filter_query, update_data
    )
