from unittest.mock import Mock
import pytest

from app.core.models import Brand
from app.core.services import ImportBrandsService


@pytest.fixture
def mock_fipe_repository():
    return Mock()


@pytest.fixture
def mock_queue_repository():
    return Mock()


@pytest.fixture
def service(mock_fipe_repository, mock_queue_repository):
    service = ImportBrandsService(mock_fipe_repository, mock_queue_repository)
    return service


def test_call_method(service, mock_fipe_repository, mock_queue_repository):
    mock_data = [Brand(code='163', name='Wake', cars=[])]
    mock_fipe_repository.fetch_brands.return_value = mock_data

    mock_queue_repository.publish_message.side_effect = [None, None]

    service()

    mock_fipe_repository.fetch_brands.assert_called_once()
    mock_queue_repository.publish_message.assert_called_with(
        "{'code': '163', 'name': 'Wake', 'cars': []}"
    )
