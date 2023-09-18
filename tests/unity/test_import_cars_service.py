from unittest.mock import Mock
import pytest

from app.core.services import ImportCarsService


@pytest.fixture
def mock_fipe_repository():
    return Mock()


@pytest.fixture
def mock_queue_repository():
    return Mock()


@pytest.fixture
def mock_cars_repository():
    return Mock()


@pytest.fixture
def service(mock_fipe_repository, mock_queue_repository, mock_cars_repository):
    service = ImportCarsService(
        mock_fipe_repository, 
        mock_queue_repository, 
        mock_cars_repository
    )
    return service


def test_call_method(service, mock_fipe_repository, mock_queue_repository):
    mock_data = [
        {'codigo': '5585', 'nome': 'AMAROK CD2.0 16V/S CD2.0 16V TDI 4x2 Die'},
        {'codigo': '5586', 'nome': 'AMAROK CD2.0 16V/S CD2.0 16V TDI 4x4 Die'}
    ]
    mock_fipe_repository.fetch_cars.return_value = mock_data

    service.import_cars('{"codigo": "163"}')

    mock_fipe_repository.fetch_cars.assert_called_once_with('163')
