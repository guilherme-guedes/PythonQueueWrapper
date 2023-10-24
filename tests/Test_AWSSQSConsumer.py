import os
import sys

import pytest
from dotenv import load_dotenv

from awsSQS.config.AWSSQSConfiguration import AWSSQSConfiguration
from awsSQS.consume.AWSSQSConsumer import AWSSQSConsumer


class Test_AWSSQSConsumer:
    @classmethod
    def setup_class(self):
        load_dotenv()
        self.__consumer = self.__create_consumer(self)

    def __create_consumer(self):
        accessKeyId = os.environ.get('ACCESS_KEY_SQS', 'accessKeyId')
        secretKey = os.environ.get('SECRET_KEY_SQS', 'secretKey')
        queue_name = os.environ.get('QUEUE', 'queue_name')
        region = 'sa-east-1'
        isFIFO = bool(os.environ.get('FIFO'), 'False')
        configuration = AWSSQSConfiguration(
            accessKeyId, secretKey, queue_name, region, isFIFO
        )
        return AWSSQSConsumer(configuration, self.__on_message_callback)

    @pytest.mark.skip(reason='to run locally')
    def test_should_listen(self):
        self.__consumer.start_listen()

    def __on_message_callback(id, body):
        print(body)
        assert body != None
        if body == 'teste':
            exit(0)
