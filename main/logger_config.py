import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler
import os

def loadLogConfigFile(configFile:str):
    logging.config.fileConfig(configFile)
    logger = logging.getLogger(os.path.basename(__file__) + __name__)
    logger.info("load logging config form ./logging.conf")


def loadLogConfigCode():
    log_dir = './logs'
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler = TimedRotatingFileHandler(filename='./logs/camping_alarm.log', when='midnight', interval=1, encoding='utf-8')
    fileHandler.setFormatter(formatter)
    fileHandler.suffix = '%Y%m%d'
    fileHandler.setLevel(logging.INFO)
    logger = logging.getLogger()
    logger.addHandler(fileHandler)
    

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(logging.DEBUG)
    logger.addHandler(streamHandler)
    logger.info("load logging config from source code")
    logger.setLevel(logging.INFO)

