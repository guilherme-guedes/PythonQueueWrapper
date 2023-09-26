from src.rabbitMQ.config.RabbitMQConfiguration import RabbitMQConfiguration

class Test_RabbitMQConfiguration:
    def test_should_create_rabbitmq_config(self):
        host = 'localhost'
        port = 3956
        routing_key = ''
        exchange = 'exchange'
        user = 'ACCESS_KEY'
        password = 'SECRET_KEY'
        queue_name = 'QUEUE'

        configuration = RabbitMQConfiguration(user, password, queue_name, host, port, exchange, routing_key)
        assert configuration != None
        assert configuration.USER == user
        assert configuration.PASSWORD == password
        assert configuration.QUEUE_NAME == queue_name
        assert configuration.HOST == host
        assert configuration.PORT == port
        assert configuration.EXCHANGE == exchange
        assert configuration.ROUTING_KEY == routing_key