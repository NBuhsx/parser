import sys, logging
from typing import Iterable, Union



def get_file_handler(pathfile:str, loggin_level, log_format:str=logging.Formatter('%(asctime)s | %(levelname)8s | %(message)s')):
    """ Файл """
    file_handler = logging.FileHandler(filename=pathfile, encoding='utf-8')
    file_handler.setLevel(level=loggin_level)
    file_handler.setFormatter(log_format)
    return file_handler


def get_stream_handler(loggin_level=logging.INFO, log_format:str=logging.Formatter('%(asctime)s | %(levelname)8s | %(message)s')):
    """ Терминал """
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(level=loggin_level)
    stream_handler.setFormatter(log_format)
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




# f"%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)
# trece = logger.add(sys.stdout, colorize=True, format="{time:HH:mm:ss} <level>{message}</level> - {name}")


config = {
    "handlers": [
        {
            "sink": sys.stdout, 
            "colorize":True, 
            "format": "<y>{time:HH:mm:ss.SSS}</y> | "
                      "<level>{level: <8}</level> | "
                      "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> |"
                      "<y>{elapsed}</y>"
        },
    ],
    "extra": {"user": "someone"}
}


# logger.debug("No matter added sinks, this message is not displayed")
# logger.info("This message however is propagated to the sinks")
# logger.error("Hello from loguru!")

# "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
#     "<level>{level: <8}</level> | "
#     "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
# {"sink": "file.log", "serialize": True, 'level':'INFO'}