from abc import abstractmethod


class Operation:
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def request_handler(self, text):
        pass
