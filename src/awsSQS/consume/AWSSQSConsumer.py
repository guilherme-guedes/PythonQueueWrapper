import logging
from time import sleep
import boto3
from botocore.exceptions import ClientError
from src.consume.BaseQueueConsumer import BaseQueueConsumer
from src.awsSQS.AWSSQSQueueFactory import AWSSQSQueueFactory

class AWSSQSConsumer(BaseQueueConsumer):
    def __init__(self, configuration, on_message):
        super().__init__(configuration)        
        self.__queue=AWSSQSQueueFactory.create_queue(configuration)
        self.__callback = on_message
        self.__pollingInterval=5
        self.__maxMessages=1
        self._generalInterval=5
        self.__listen=False

    #def on_message(message_id, body):

    def start_listen(self):
        logging.info('Starting consumer...')
        try:
            while True:
                self.receive_messages()
                sleep(self._generalInterval)
        except ClientError as error:
            logging.exception("Couldn't receive messages from queue: %s")
            raise error        

    def stop_listen(self):
        self.__listen = False
        logging.info('Stopping consumer...')

    def receive_messages(self):
        messages = []
        self.__listen = True
        try:
            while self.__listen:
                messages = self.__queue.receive_messages(
                    MessageAttributeNames=['All'],
                    MaxNumberOfMessages=self.__maxMessages,
                    WaitTimeSeconds=self.__pollingInterval
                )
                
                for msg in messages:
                    logging.debug("Received message: %s: %s", msg.message_id, msg.body)
                    self.__callback(msg.message_id, msg.body)

        except ClientError as error:
            logging.exception("Couldn't receive messages from queue: %s", self.__queue)
            raise error

