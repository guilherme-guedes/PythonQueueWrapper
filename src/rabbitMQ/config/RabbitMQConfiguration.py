from src.config.PubSubConfiguration import PubSubConfiguration


class RabbitMQConfiguration(PubSubConfiguration):
    def __init__(
        self, user, password, queue_name, host, port, exchange, routingKey
    ):
        super().__init__(user, password, queue_name)
        self.HOST = host
        self.PORT = port
        self.EXCHANGE = exchange
        self.ROUTING_KEY = routingKey
