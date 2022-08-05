
# from imports import logger

# import os.path
# import more_itertools

# from concurrent.futures import ThreadPoolExecutor



# from baseParser.configure.base_config import parse_config
# from baseParser.write_read import read_rows, read_json
# from baseParser.control import ProxyPull

# from Yarche.configure.config import Config, get_config
# from Yarche.build.build import Soft




# def main(configureFile):
#     logger.info("Программа стартует")

#     config:Config = get_config(
#         data=parse_config(pathfile=configureFile))
    
#     logger.add(
#         config.system.pathFileLogging,
#         backtrace=True, diagnose=True)
#     logger.info('Получен конфиг')
    

#     # Proxy 
#     if config.system.use_proxy:
#         proxy = read_rows(
#                         pathfile=config.system.pathFileProxy,
#                         slice=slice(0, -1))
#     else:
#         proxy = []

    
#     # Потоки
#     if config.system.use_thread:
#         logger.info("Запуск многопоточного режима")
#         with ThreadPoolExecutor(max_workers=config.system.thread) as pool:
#             for arg_pool in zip(
#                 more_itertools.divide(config.system.thread, config.prod.Adress),
#                 more_itertools.divide(config.system.thread, proxy)):

#                 config.prod.Adress = iter(arg_pool[0])

#                 pool.submit(
#                     fn=Soft(
#                         config=config,
#                         proxy=ProxyPull(proxies=arg_pool[1])).center, itap=1)
#     else:
#         logger.info("Запуск однопоточного режима")
#         Soft(
#             config=config,
#             proxy=ProxyPull(proxies=proxy)).center(itap=0)
        

      

                
            

# if __name__ == '__main__':
#     main(
#         configureFile=os.path.dirname(__file__) + '/configure/config.json' 
#     )
#     # category = read_json(
#     #     pathfile=r'C:\Users\ole lukoie\Desktop\my_parser\Yarche\result\result_Россия, Москва, Вересаева 10.json',
#     # )

# #"http://127.0.0.1:8080"


import more_itertools

from loguru import logger

from concurrent.futures import ThreadPoolExecutor
from pydantic import ValidationError, parse_file_as
from datetime import datetime


from settings.config_logger import logger
from settings.read_write import read_rows
from settings.contol import ProxyPull
from configure.config import Config
from build.build import Soft







def main(path_configure_file:str):
    logger.info("Программа стартует")
    
    try:
        config = parse_file_as(Config, path=path_configure_file)
    except ValidationError as error:
        logger.error(error.json())
    else:
        logger.info('Получен конфиг')
        if config.setting_system.logging:
            print(config.setting_system.path_dir_logging.joinpath(
                f'log_{datetime.now().strftime("%d-%m-%Y_%H:%M")}.log'
            ))
            logger.add(
                config.setting_system.path_dir_logging.joinpath(
                    f'log_{datetime.now().strftime("%d-%m-%Y_%H:%M")}.log'),
                backtrace=True, 
                diagnose=True)

        if config.setting_system.use_proxy:
            proxy = read_rows(
                        pathfile=config.setting_system.path_file_proxy,
                        slice=slice(0, -1))
        else:
            proxy = []

        # Потоки
        if config.setting_system.use_thread:
            logger.info("Запуск многопоточного режима")
            with ThreadPoolExecutor(max_workers=config.setting_system.thread) as pool:
                for arg_pool in zip(
                    more_itertools.divide(config.setting_system.thread, config.parser.parse_adress),
                    more_itertools.divide(config.setting_system.thread, proxy)):

                    config.parser.Adress = iter(arg_pool[0])

                    pool.submit(Soft(
                        config=config,
                        proxy=
                    ))
        else:
            logger.info("Запуск однопоточного режима")
            Soft(
                config=config,
                proxy=ProxyPull(proxies=proxy)).center(itap=0)



if __name__ == "__main__":
    main(path_configure_file='Yarche/configure/config.json')