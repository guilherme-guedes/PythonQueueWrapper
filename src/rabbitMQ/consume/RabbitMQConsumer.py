import pika
import logging
from src.consume.BaseQueueConsumer import BaseQueueConsumer
from src.rabbitMQ.RabbitMQChannelFactory import RabbitMQChannelFactory
from src.rabbitMQ.RabbitMQConnectionFactory import RabbitMQConnectionFactory

class RabbitMQConsumer(BaseQueueConsumer):
    def __init__(self, configuration, on_message):
        super().__init__(configuration)      
        self.__callback=on_message          
        self.__channel=RabbitMQChannelFactory.create_channel(configuration) 
        self.__configure_queue()

    #def on_message(ch, method, props, body):
     
    def __configure_queue(self):
        logging.debug('Queue ' + self._configuration.QUEUE_NAME)
        self.__channel.queue_declare( queue=self._configuration.QUEUE_NAME, durable=True )

        self.__channel.basic_consume(
            queue=self._configuration.QUEUE_NAME,
            auto_ack=True,
            on_message_callback=self.__callback
        )

    def start_listen(self):
        logging.info('Starting consumer...')
        self.__channel.start_consuming()

    def stop_listen(self):
        logging.info('Stopping consumer...')
        self.__channel.stop_consuming()