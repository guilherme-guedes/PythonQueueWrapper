import logging
from abc import ABC

import pika

from rabbitMQ.RabbitMQConnectionFactory import RabbitMQConnectionFactory


class RabbitMQChannelFactory(ABC):
    @staticmethod
    def create_channel(configuration):
        logging.info('creating channel...')
        connection = RabbitMQConnectionFactory.create_connection(configuration)
        channel = connection.channel()
        logging.info('Channel created.')
        return channel
