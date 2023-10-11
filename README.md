
# Python Simple Queue Wrapper


Simple lib for pub/sub to queue brokers
  

## Supported

* RabbitMQ

* Amazon SQS
  

## Development

`poetry shell` to start dev env.
  

### Tasks

Run tasks with poetry eg: `task lint`

*  `lint` = Lint verifications and diff

*  `format` = Apply lint correction and format

*  `docs` = Run local docs server

*  `test` = Run tests

  

## Testing

Some tests will not run automatically (only locally).

For run it, there will be necessary a `.env` file with some attributes.

eg:

```
HOST_RABBIT=localhost
EXCHANGE_RABBIT={exchange_teste}
USER_RABBIT={user}
PASSWORD_RABBIT={password} 

ACCESS_KEY_SQS={access_key}
SECRET_KEY_SQS={secret_key} 

QUEUE={queue}
LOGGER_LEVEL=DEBUG
```