from .bot import Robot
from .message import *
from .receiveHandler import ReceiveHandler
from typing import Final
import requests
import json
from .bot import *
from ..secret import TELEGRAM_KEY
from .BotReceiveHandler import BotReceiveHandler

TELEGRAM_API_HOST :Final = "https://api.telegram.org"
TELEGRAM_API_UPDATE :Final = "https://api.telegram.org/{bot}/getUpdates"

class Telegram(Robot):

    def __init__(self, key:str):
        super().__init__(RobotType.TELEGRAM, key)

    def sendMessage(self, message:ChatMessage):
        pass

    def readMessage(self, receiveHandler:ReceiveHandler):
        while True:
            response = requests.get(TELEGRAM_API_UPDATE.format(bot=self.key))
            print("status code:", response.status_code)
            print("body", response.content)
            print("encoding", response.encoding)
            print("encoding", response.text)
            print("json", json.dumps(response.json(),  sort_keys=True, indent=4))
            resBody = response.json()

            if type(resBody) == dict:
                print(dict)
                result:list = resBody.get('result', [])
                for update in result:
                    id = update['channel_post']['chat']['id']
                    user= update['channel_post']['sender_chat']['username']
                    message=update['channel_post']['text']
                    receiveMessage = createReceiveMessage(id, user, message)
                    print(receiveMessage)
                    print(receiveHandler)
                    receiveHandler.received(self, receiveMessage)
            break
# print(resBody.keys())
bot = Telegram(TELEGRAM_KEY)
re = BotReceiveHandler()
bot.readMessage(re)