from .message import ChatMessage
from abc import *
class ReceiveHandler(metaclass=ABCMeta):
    
    @abstractmethod
    def received(self, soruce, message:ChatMessage):
        pass