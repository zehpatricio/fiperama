import pytest
import pika
from unittest.mock import MagicMock
from app.repository import QueueRepository


@pytest.fixture
def mock_rabbitmq_channel():
    channel = MagicMock(spec=pika.channel.Channel)
    return channel


@pytest.fixture
def mock_rabbitmq_connection(mock_rabbitmq_channel):
    mock_conn = MagicMock(spec=pika.BlockingConnection)
    mock_conn.channel.return_value = mock_rabbitmq_channel
    return mock_conn


@pytest.fixture(autouse=True)
def mock_rabbitmq_blocking_connection(monkeypatch, mock_rabbitmq_connection):
    def mock_blocking_connection(*args, **kwargs):
        return mock_rabbitmq_connection

    monkeypatch.setattr(pika, "BlockingConnection", mock_blocking_connection)


def test_initialize_connection(mock_rabbitmq_channel):
    # Initialize a QueueRepository instance
    queue_repo = QueueRepository(
        host="localhost",
        port=5672,
        username="test_user",
        password="test_password",
        queue_name="test_queue"
    )

    # Verify that the connection and channel were created
    mock_rabbitmq_channel.queue_declare.assert_called_once_with(
        queue='test_queue'
    )

    assert queue_repo.host == "localhost"
    assert queue_repo.port == 5672
    assert queue_repo.username == "test_user"
    assert queue_repo.password == "test_password"
    assert queue_repo.queue_name == "test_queue"
