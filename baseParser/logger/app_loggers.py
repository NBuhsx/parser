
import logging
from typing import Iterable, Union




# class CustomFormatter(logging.Formatter):
#     grey = "\x1b[90m"
#     green = "\x1b[92m"
#     yellow = "\x1b[33;20m"
#     red = "\x1b[31;20m"
#     bold_red = "\x1b[31;1m"
#     reset = "\x1b[0m"

#     def __init__(self, fmt:Union[str, None]=None) -> None:
#         super().__init__(fmt)

#         self.FORMATS = {
#             logging.DEBUG: CustomFormatter.grey + fmt + CustomFormatter.reset,
#             logging.INFO: CustomFormatter.green + fmt + CustomFormatter.reset,
#             logging.WARNING: CustomFormatter.yellow + fmt + CustomFormatter.reset,
#             logging.ERROR: CustomFormatter.red + fmt + CustomFormatter.reset,
#             logging.CRITICAL: CustomFormatter.bold_red + fmt + CustomFormatter.reset
#         }

#     def format(self, record):
#         return logging.Formatter(
#             fmt=self.FORMATS.get(record.levelno)).format(record)



def get_file_handler(pathfile:str, loggin_level, log_format:str='%(asctime)s | %(levelname)8s | %(message)s'):
    """ Файл """
    file_handler = logging.FileHandler(filename=pathfile)
    file_handler.setLevel(level=loggin_level)
    file_handler.setFormatter(logging.Formatter(log_format))
    return file_handler

def get_stream_handler(loggin_level=logging.INFO, log_format:str='%(asctime)s | %(levelname)8s | %(message)s'):
    """ Терминал """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=loggin_level)
    stream_handler.setFormatter(logging.Formatter(log_format))
    return stream_handler

def get_logger(name:str, handlers:Union[Iterable, None]=None, filters:Union[Iterable, None]=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if handlers:
        for handler in handlers:
            logger.addHandler(handler)
    if filters:
        for filter in filters:
            logger.addFilter(filter)
    return logger

