from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_import_data_success():
    response = client.get('/brands')
    
    assert response.status_code == 200
    assert 'brands' in response.json()


def test_import_data_service_failure():
    
    response = client.get('/brands')
    assert response.status_code == 500
