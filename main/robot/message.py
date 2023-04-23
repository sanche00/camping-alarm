from enum import Enum

class MessageType(Enum):
    RECEIVE = 1
    SEND = 2

class ChatMessage:
    id:str
    user:str
    message:str
    type:MessageType

    def __init__(self, id:str, user:str, message:str, type:MessageType):
        self.id = id
        self.user = user
        self.message = message
        self.type = type

def createReceiveMessage(id:str, user:str, message:str):
    return ChatMessage(id, user, message, MessageType.RECEIVE)
