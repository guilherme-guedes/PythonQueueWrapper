import os

import pytest
from dotenv import load_dotenv

from awsSQS.config.AWSSQSConfiguration import AWSSQSConfiguration
from awsSQS.publish.AWSSQSPublisher import AWSSQSPublisher


class Test_AWSSQSPublisher:
    @classmethod
    def setup_class(self):
        load_dotenv()
        self.__publisher = self.__create_publisher(self)

    def __create_publisher(self):
        accessKeyId = os.environ.get('ACCESS_KEY_SQS')
        secretKey = os.environ.get('SECRET_KEY_SQS')
        queue_name = os.environ.get('QUEUE')
        region = 'sa-east-1'
        isFIFO = bool(os.environ.get('FIFO'))
        configuration = AWSSQSConfiguration(
            accessKeyId, secretKey, queue_name, region, isFIFO
        )
        return AWSSQSPublisher(configuration)

    @pytest.mark.skip(reason='to run locally')
    def test_should_publish(self):
        assert self.__publisher.publish('test message') == True
