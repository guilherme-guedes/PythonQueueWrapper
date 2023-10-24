import os

import pytest
from dotenv import load_dotenv

from rabbitMQ.config.RabbitMQConfiguration import RabbitMQConfiguration
from rabbitMQ.publish.RabbitMQPublisher import RabbitMQPublisher


class Test_RabbitMQPublisher:
    @classmethod
    def setup_class(self):
        load_dotenv()
        self.__publisher = self.__create_publisher(self)

    def __create_publisher(self):
        host = os.environ.get('HOST_RABBIT', 'localhost')
        exchange = os.environ.get('EXCHANGE_RABBIT', 'exchange')
        user = os.environ.get('USER_RABBIT', 'user')
        password = os.environ.get('PASSWORD_RABBIT', 'password')
        queue = os.environ.get('QUEUE', 'queue')
        port = 5672
        configuration = RabbitMQConfiguration(
            user, password, queue, host, port, exchange, ''
        )
        return RabbitMQPublisher(configuration)

    @pytest.mark.skip(reason='to run locally')
    def test_should_publish(self):
        assert self.__publisher.publish('test message') == True
