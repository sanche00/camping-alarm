from .bot import Robot
from .receiveHandler import ReceiveHandler
from .message import ChatMessage

class BotReceiveHandler(ReceiveHandler):
    def received(self, soruce:Robot, message:ChatMessage):
        print(soruce)
        print(message)
