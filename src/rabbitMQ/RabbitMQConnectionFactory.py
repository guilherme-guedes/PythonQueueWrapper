from abc import ABC

import pika


class RabbitMQConnectionFactory(ABC):
    @staticmethod
    def create_connection(configuration):
        connection_params = pika.ConnectionParameters(
            host=configuration.HOST,
            port=configuration.PORT,
            credentials=pika.PlainCredentials(
                username=configuration.USER, password=configuration.PASSWORD
            ),
        )
        return pika.BlockingConnection(connection_params)
