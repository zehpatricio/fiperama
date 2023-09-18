from unittest.mock import Mock
import pytest

from app.core.services import ImportCarsService
from app.core.models import Brand, Car


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


def test_call_method(service, mock_fipe_repository, mock_cars_repository):
    car_1 = {
        'code': '5585', 
        'name': 'AMAROK CD2.0 16V/S CD2.0 16V TDI 4x2 Die'
    }
    mock_data = [car_1]
    mock_fipe_repository.fetch_cars.return_value = mock_data

    service.import_cars(
        None, None, None, b'{"code": "163", "name": "brand", "cars": []}'
    )
    
    mock_fipe_repository.fetch_cars.assert_called_once_with('163')
    mock_cars_repository.insert.assert_called_with(
        Brand(code='163', name='brand', cars=[{'code': '5585', 'name': 'AMAROK CD2.0 16V/S CD2.0 16V TDI 4x2 Die'}])
    )
