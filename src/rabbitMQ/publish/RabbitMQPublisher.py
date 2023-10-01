import logging

import pika

from base.publish.BaseQueuePublisher import BaseQueuePublisher
from rabbitMQ.RabbitMQChannelFactory import RabbitMQChannelFactory
from rabbitMQ.RabbitMQConnectionFactory import RabbitMQConnectionFactory


class RabbitMQPublisher(BaseQueuePublisher):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.__exchange = configuration.EXCHANGE
        self.__routing_key = configuration.ROUTING_KEY
        self.__channel = RabbitMQChannelFactory.create_channel(configuration)

    def publish(self, msg):
        logging.debug('Publishing to' + self.__exchange)
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=msg,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        logging.debug('Published.')
