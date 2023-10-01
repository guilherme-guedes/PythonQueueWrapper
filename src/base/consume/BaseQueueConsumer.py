from abc import ABC, abstractmethod

from base.config.PubSubConfiguration import PubSubConfiguration


class BaseQueueConsumer(ABC):
    def __init__(self, configuration):
        self._configuration = configuration

    @abstractmethod
    def start_listen(self):
        pass

    @abstractmethod
    def stop_listen(self):
        pass
