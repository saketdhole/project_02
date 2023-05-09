import os
import logging


class logen:

    @staticmethod
    def configure_logging():

        logger = logging.getLogger("debuglogger")
        logger.setLevel(logging.INFO)
        filepath = os.path.join(os.getcwd(), 'logs','debug.info')                      # create a file handler
        file_handler = logging.FileHandler(filepath, mode='a', encoding='UTF-8')
        formatter = logging.Formatter(
            '"%(asctime)s: %(levelname)s: %(name)s :%(message)s"')                      # file_handler.setLevel(logging.DEBUG) # create a logging format
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)                                                 # add the handler to the logger
        return logger