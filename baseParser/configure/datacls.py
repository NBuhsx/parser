import os, sys
from dataclasses import dataclass, InitVar
from datetime import datetime
from typing import Union





@dataclass
class settinngSystem:
    use_thread:bool = False
    thread:int = 10
    use_proxy:bool = False
    pathFileProxy:InitVar[str] = 'defaut'
    logging:bool = True 
    pathFileLogging:InitVar[str] = 'defaut'

    def __post_init__(self, pathFileProxy:Union[str, bool], pathFileLogging:Union[str, bool]):
        if self.use_proxy:
            self.self.pathFileProxy = os.path.abspath(os.path.dirname(sys.argv[0])) + \
                    r'\proxy\use.txt' if pathFileProxy == 'defaut' else pathFileProxy
          
        if self.logging:
            if pathFileLogging == 'defaut':
                if not os.path.exists(os.path.abspath(os.path.dirname(sys.argv[0])) + '\logs'):
                    os.mkdir(os.path.abspath(os.path.dirname(sys.argv[0])) + '\logs')

                self.pathFileLogging =  os.path.abspath(os.path.dirname(sys.argv[0])) + \
                    f'\logs\log_{datetime.now().strftime("%d-%m-%Y %H.%M")}.log'
            else:
                self.pathFileLogging = pathFileLogging
           



@dataclass
class SendEmail:
    typeConnect:str
    server:str
    port:int
    login:str
    password:str



@dataclass
class Config:
    base_url:str





    