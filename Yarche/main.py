

from email import header
from imports import logger

import os.path
import more_itertools

from concurrent.futures import ThreadPoolExecutor



from baseParser.configure.base_config import parse_config
from baseParser.write_read import read_rows, read_json
from baseParser.control import ProxyPull

from Yarche.configure.config import Config, get_config
from Yarche.build.buld import ParseYarcheProductCategory




def main(configureFile):
    logger.info("Программа стартует")

    config:Config = get_config(
        data=parse_config(pathfile=configureFile))
    
    logger.add(
        config.system.pathFileLogging,
        backtrace=True, diagnose=True)
    logger.info('Получен конфиг')
    



    # Proxy 
    if config.system.use_proxy:
        proxy = read_rows(
                        pathfile=config.system.pathFileProxy,
                        slice=slice(0, -1))
    else:
        proxy = []

    
    # Потоки
    if config.system.use_thread:
        logger.info("Запуск многопоточного режима")
        with ThreadPoolExecutor(max_workers=config.system.thread) as pool:
            for arg_pool in zip(
                more_itertools.divide(config.system.thread, config.prod.Adress),
                more_itertools.divide(config.system.thread, proxy)):

                config.prod.Adress = iter(arg_pool[0])

                pool.submit(
                    fn=ParseYarcheProductCategory(
                        config=config,
                        proxy=ProxyPull(proxies=arg_pool[1])).center, itap=1)
    else:
        logger.info("Запуск однопоточного режима")
        ParseYarcheProductCategory(
            config=config,
            proxy=ProxyPull(proxies=proxy)).center(itap=0)
        

      

                
            

if __name__ == '__main__':
    main(
        configureFile=os.path.dirname(__file__) + '\configure\config.json' 
    )
    # category = read_json(
    #     pathfile=r'C:\Users\ole lukoie\Desktop\my_parser\Yarche\result\result_Россия, Москва, Вересаева 10.json',
    # )
  

      

 
      
    
    # ParseYarcheProductCategory.result_csv(category)

    
 
 
