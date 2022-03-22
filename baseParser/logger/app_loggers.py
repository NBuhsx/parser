import logging
from functools import reduce

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

def get_file_handler(pathfile:str, loggin_level:logging.DEBUG, log_format:str=_log_format):
    file_handler = logging.FileHandler(filename=pathfile)
    file_handler.setLevel(level=loggin_level)
    file_handler.setFormatter(logging.Formatter(log_format))
    return file_handler

def get_stream_handler(loggin_level:logging.DEBUG, log_format:str=_log_format):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=loggin_level)
    stream_handler.setFormatter(logging.Formatter(log_format))
    return stream_handler

def get_logger(name, *handlers):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    reduce(
        logger.addHandler,
        handlers
    )
    return logger









