from base.config.PubSubConfiguration import PubSubConfiguration


class AWSSQSConfiguration(PubSubConfiguration):
    def __init__(
        self,
        accessKeyId,
        secretKey,
        queue_name,
        region,
        is_FIFO_queue=False,
        msg_group_id=None,
    ):
        super().__init__(accessKeyId, secretKey, queue_name)
        self.REGION = region
        self.IS_FIFO_QUEUE = is_FIFO_queue

        if msg_group_id == None:
            self.MESSAGE_GROUP_ID = str(queue_name + '_GROUP')
        else:
            self.MESSAGE_GROUP_ID = msg_group_id
