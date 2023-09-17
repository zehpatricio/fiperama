import unittest
import pytest
from requests.exceptions import HTTPError
from unittest.mock import MagicMock, patch

from app.repository import FipeRepository, CouldNotConnectToFipeAPI


API_BASE_URL = "https://api.fipe.com"


@pytest.fixture
def api_repo():
    return FipeRepository(API_BASE_URL)


@patch('requests.get')
def test_get_success(mock_get, api_repo):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"marca": "tesla"}]
    mock_get.return_value = mock_response

    response_json = api_repo.get("marcas")

    mock_get.assert_called_once_with("https://api.fipe.com/marcas", params=None)
    assert response_json == [{"marca": "tesla"}]


@patch('requests.get')
def test_get_http_error(mock_get, api_repo):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = HTTPError()
    mock_get.return_value = mock_response

    with unittest.TestCase().assertRaises(CouldNotConnectToFipeAPI) as cm:
        api_repo.get("marcas/123")

    assert str(cm.exception) == (
        "Could not connect to Fipe API. HTTP status code: 404"
    )
    assert cm.exception.status_code == 404

