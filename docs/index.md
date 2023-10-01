# Simple Queue Wrapper

Lib for simple integration with queue brokers.

## Supported Brokers

* `RabbitMQ`  
* `Amazon SQS` 

## Basic Usage with RabbitMQ

### Consumer 
```
def __on_message_callback(ch, method, props, body):
    do_somenthing(body)
    
configuration = RabbitMQConfiguration(
    user, password, queue, host, port, exchange, routing_key
)

consumer = RabbitMQConsumer(configuration, __on_message_callback)
consumer.start_listen()
```

### Producer 
```
def __on_message_callback(ch, method, props, body):
    do_somenthing(body)
    
configuration = RabbitMQConfiguration(
    user, password, queue, host, port, exchange, routing_key
)

consumer = RabbitMQConsumer(configuration, __on_message_callback)
consumer.start_listen()
```