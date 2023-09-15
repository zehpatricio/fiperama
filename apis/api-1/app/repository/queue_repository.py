import pika

class QueueRepository:
    def __init__(self, host, port, username, password, queue_name):
        """
        Initialize a connection to RabbitMQ and declare a queue.

        Args:
            host (str): RabbitMQ server hostname.
            port (int): RabbitMQ server port.
            username (str): RabbitMQ username.
            password (str): RabbitMQ password.
            queue_name (str): Name of the queue to work with.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.queue_name = queue_name

        # Establish a connection to RabbitMQ
        credentials = pika.PlainCredentials(username, password)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host, 
                port=self.port, 
                credentials=credentials
            )
        )
        self.channel = self.connection.channel()
        
        # Declare the queue
        self.channel.queue_declare(queue=self.queue_name)

    def publish_message(self, message):
        """
        Publish a message to the specified queue.

        Args:
            message (str): The message to be published.
        """
        self.channel.basic_publish(
            exchange='', 
            routing_key=self.queue_name, 
            body=message
        )
        print(f" [x] Sent '{message}'")

    def consume_messages(self, callback):
        """
        Start consuming messages from the specified queue.

        Args:
            callback (function): A callback function to process received messages.

        Example:
            def message_callback(ch, method, properties, body):
                print(f" [x] Received '{body}'")
            rabbitmq.consume_messages(message_callback)
        """
        self.channel.basic_consume(
            queue=self.queue_name, 
            on_message_callback=callback, 
            auto_ack=True
        )
        print(f" [*] Waiting for messages in queue '{self.queue_name}'")
        self.channel.start_consuming()

    def close_connection(self):
        """
        Close the RabbitMQ connection.
        """
        self.connection.close()
