import imports 

import os.path, sys


from baseParser.configure.base_config import parse_config, write_config
from Yarche.configure.config import Config, get_config
from concurrent.futures import ThreadPoolExecutor





def main(configureFile:str):
    config:Config = get_config(
        data=parse_config(
            pathfile=configureFile)
    )







    
    # конфиг получен
    # if config.system.use_thread:
    #     with ThreadPoolExecutor(
    #         max_workers=config.system.thread
    #     ) as pool:
    #         for pool in 
    

    
  
    


    
   





if __name__ == '__main__':
    main(
        configureFile=os.path.dirname(__file__) + '\configure\config.json'
    )





