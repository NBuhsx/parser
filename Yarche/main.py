import imports


import logging
import os.path, sys

from baseParser.logger.app_loggers import get_logger, get_file_handler, get_stream_handler
from baseParser.configure.base_config import parse_config, write_config
from baseParser.parse import Parse
from Yarche.configure.config import Config, get_config
from concurrent.futures import ThreadPoolExecutor


logger=get_logger(
        __name__,
        get_stream_handler(
            loggin_level=logging.DEBUG
            ))


def main(configureFile:str):
    logger.warning("Сатана")
    config = get_config(
        data=parse_config(pathfile=configureFile))

    logger.addHandler(
        logging.FileHandler(
            filename=config.system.pathFileLogging
        )
    )
    print('ff')
    logger.info("Сатана")

  


 







    
    # конфиг получен
    # if config.system.use_thread:
    #     with ThreadPoolExecutor(
    #         max_workers=config.system.thread
    #     ) as pool:
    #         for pool in 
    

    
  
if __name__ == '__main__':
    Parse.check(
        func=main,
        logger=logger,
        configureFile=os.path.dirname(__file__) + '\configure\config.json'
    )
        
    