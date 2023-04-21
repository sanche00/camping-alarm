from enum import Enum
from abc import *
class RobotType(Enum):
    TELEGRAM = 1


class Robot(metaClass=ABCMeta):
    type:RobotType
    key:str
    extends:dict

    @abstractmethod
    def sendMessage(self, strMessage:str):
        pass
