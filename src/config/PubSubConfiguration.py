from abc import ABC

class PubSubConfiguration(ABC):
    def __init__(self, user, password, queue_name) -> None:        
        self.USER=user
        self.PASSWORD=password
        self.QUEUE_NAME=queue_name