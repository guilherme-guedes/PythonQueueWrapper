from src.awsSQS.config.AWSSQSConfiguration import AWSSQSConfiguration

class Test_AWSSQSConfiguration:
    def test_should_create_aws_config(self):
        user = 'ACCESS_KEY'
        password = 'SECRET_KEY'
        queue_name = 'QUEUE'
        region = 'sa-east-1'

        configuration = AWSSQSConfiguration(user, password, queue_name, region)
        assert configuration != None
        assert configuration.USER == user
        assert configuration.PASSWORD == password
        assert configuration.QUEUE_NAME == queue_name
        assert configuration.REGION == region