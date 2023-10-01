from src.config.PubSubConfiguration import PubSubConfiguration


class AWSSQSConfiguration(PubSubConfiguration):
    def __init__(self, accessKeyId, secretKey, queue_name, region):
        super().__init__(accessKeyId, secretKey, queue_name)
        self.REGION = region
