from .logger_config import loadLogConfigCode
import atexit
import logging

mainlogger = loadLogConfigCode()

def main():
    mainlogger.info("start camping alarm !!!!")
    atexit.register(handle_exit)  


def handle_exit():
    mainlogger.info("finished camping alarm")

if __name__ == "__main__":
    main()



