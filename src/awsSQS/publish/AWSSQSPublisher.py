import hashlib
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
        logging.debug('Publishing to' + str(self.__queue))

        hash = hashlib.md5(msg.encode('utf-8')).hexdigest()

        try:
            response = self.__queue.send_message(
                MessageBody=msg,
                MessageGroupId=self._config.MESSAGE_GROUP_ID
                if self._config.IS_FIFO_QUEUE
                else None,
                MessageDeduplicationId=hash
                if self._config.IS_FIFO_QUEUE
                else None,
            )
        except ClientError as error:
            logging.exception('Publish message failed: %s', msg)
            raise error
        else:
            logging.debug('Published.')
            return response != None and response['MessageId'] != None
