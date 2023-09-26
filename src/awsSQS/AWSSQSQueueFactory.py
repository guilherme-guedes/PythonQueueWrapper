import logging
from abc import ABC
import boto3
from botocore.exceptions import ClientError

class AWSSQSQueueFactory(ABC):  

    @staticmethod       
    def create_queue(configuration):
        try:
            sqs = AWSSQSQueueFactory.__create_sqs(configuration)
            queue = sqs.create_queue( QueueName=configuration.QUEUE_NAME, Attributes={} )
            logging.info("Created queue '%s' with URL=%s", configuration.QUEUE_NAME, queue.url)
        except ClientError as error:
            logging.exception("Couldn't create queue named '%s'.", configuration.QUEUE_NAME)
            raise error
        else:
            return queue        
     
    @staticmethod  
    def __create_sqs(configuration):
        return boto3.resource('sqs', region_name=configuration.REGION,
                              aws_access_key_id=configuration.USER,
                              aws_secret_access_key=configuration.PASSWORD)