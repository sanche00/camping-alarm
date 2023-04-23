from enum import Enum
from abc import *
from .message import ChatMessage
from .receiveHandler import ReceiveHandler

class RobotType(Enum):
    TELEGRAM = 1


class Robot(metaclass=ABCMeta):
    type:RobotType
    key:str
    # extends:dict

    # def __init_subclass__(cls, handler=None):
    #     super().__init_subclass__()
    #     cls.handler = handler

    def __init__(self, type:RobotType, key:str):
        self.type = type
        self.key = key

    @abstractmethod
    def sendMessage(self, message:ChatMessage):
        pass

    @abstractmethod
    def readMessage(self, receiveHandler:ReceiveHandler):
        pass
