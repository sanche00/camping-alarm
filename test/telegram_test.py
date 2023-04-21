import unittest

from main.robot.telegram import Telegram
from main.secret import TELEGRAM_KEY

class TestTelegramBot(unittest.TestCase):
    telegramBot:Telegram

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.telegramBot = Telegram(key=TELEGRAM_KEY)
