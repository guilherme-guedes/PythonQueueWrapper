from abc import ABC, abstractmethod
from src.config.PubSubConfiguration import PubSubConfiguration


class BaseQueuePublisher(ABC):
    def __init__(self, configuration):
        self._config = configuration

    @abstractmethod
    def publish(self, msg):
        pass
