from .robot import *
from typing import Final
import requests
from ..secret import TELEGRAM_KEY
TELEGRAM_API_HOST :Final = "https://api.telegram.org"
TELEGRAM_API_UPDATE :Final = "https://api.telegram.org/{bot}/getUpdates"

class Telegram(Robot):

    def __init__(self, type:RobotType, key:str):
        super().__init__(RobotType.TELEGRAM, key)
        # self.type=type
        # self.key=key

    def sendMessage(self, strMessage:str):
        pass

    def readMessage(self, callback):
        pass
    

response = requests.get(TELEGRAM_API_UPDATE.format(bot=TELEGRAM_KEY))

print("status code:", response.status_code)
print("body", response.content)
