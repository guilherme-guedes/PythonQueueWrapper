import os
import sys

import pytest
from dotenv import load_dotenv

from rabbitMQ.config.RabbitMQConfiguration import RabbitMQConfiguration
from rabbitMQ.consume.RabbitMQConsumer import RabbitMQConsumer


class Test_RabbitMQConsumer:
    @classmethod
    def setup_class(self):
        load_dotenv()
        self.__consumer = self.__create_consumer(self)

    def __create_consumer(self):
        host = os.environ.get('HOST_RABBIT', 'localhost')
        exchange = os.environ.get('EXCHANGE_RABBIT')
        user = os.environ.get('USER_RABBIT')
        password = os.environ.get('PASSWORD_RABBIT')
        queue = os.environ.get('QUEUE')
        port = 5672
        configuration = RabbitMQConfiguration(
            user, password, queue, host, port, exchange, ''
        )
        return RabbitMQConsumer(configuration, self.__on_message_callback)

    @pytest.mark.skip(reason='to run locally')
    def test_should_listen(self):
        self.__consumer.start_listen()

    def __on_message_callback(ch, method, props, body):
        print(body)
        assert body != None
        if body != None:
            ch.cancel()
            ch.stop_consuming()
