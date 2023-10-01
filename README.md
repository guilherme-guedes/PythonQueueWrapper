# Python Simple Queue Wrapper

Simple lib for pub/sub to queue brokers

## Supported
* RabbitMQ
* Amazon SQS

## Tasks
* `lint` = Lint verifications and diff
* `format` = Apply lint correction and format
* `docs` = Run local docs server
* `test` = Run tests

## Testing
Some tests will not run automatically (only locally).
For run it, there will be necessary a `.env` file with some attributes.
eg:
``
HOST=localhost
EXCHANGE={exchange_teste}
USER={user}
PASSWORD={password}
QUEUE={queue}
LOGGER_LEVEL=DEBUG
``


