import imports


import logging
import os.path, sys

from baseParser.logger.app_loggers import get_logger, get_file_handler, get_stream_handler
from baseParser.configure.base_config import parse_config
from baseParser.control import check
from baseParser.write_read import read_rows
from baseParser.control import ProxyPull

from Yarche.configure.config import Config, get_config
from Yarche.buld import ParseYarcheProductCategory
    


logger = get_logger(
    name=__name__,
    handlers=[get_stream_handler(
        loggin_level=logging.DEBUG,
        log_format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
            )])



def main(configureFile:str):
    logger.info("Программа стартует")

    config:Config = get_config(
        data=parse_config(pathfile=configureFile))

    logger.addHandler(
        hdlr=get_file_handler(pathfile=config.system.pathFileLogging, loggin_level=logging.DEBUG)
    )
    logging.info("Создан лог для записи")

    if config.system.use_proxy:
        proxy = ProxyPull(
            proxies=read_rows(
                pathfile=config.system.pathFileProxy,
                slice=slice(0, -1)
            ))
    else:
        proxy = ProxyPull(noProxy=1)
    
    parser = ParseYarcheProductCategory(
        config=config,
        proxy=proxy)
    parser.CENTER()
    
    


   

  
if __name__ == '__main__':
    check(
        func=main,
        logger=logger,
        configureFile=os.path.dirname(__file__) + '\configure\config.json'
    )


# Парсер Концепт 
    # Cтарт
    ### --- Рарсер
    # Получение результата

