import logging

import boto3
from botocore.exceptions import ClientError

from awsSQS.AWSSQSQueueFactory import AWSSQSQueueFactory
from base.publish.BaseQueuePublisher import BaseQueuePublisher


class AWSSQSPublisher(BaseQueuePublisher):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.__queue = AWSSQSQueueFactory.create_queue(configuration)

    def publish(self, msg):
        logging.debug('Publishing to' + self.__queue)
        try:
            response = self.__queue.send_message(
                MessageBody=msg, MessageAttributes={}
            )
        except ClientError as error:
            logging.exception('Publish message failed: %s', msg)
            raise error
        else:
            logging.debug('Published.')
            return response != None and response['MessageId'] != None
