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
    pathDirResult:InitVar[str] = 'defaut'

    def __post_init__(self, 
            pathFileProxy:Union[str, bool], 
            pathFileLogging:Union[str, bool],
            pathDirResult:Union[str, bool]):

        pathDIR = os.path.abspath(os.path.dirname(sys.argv[0]))

        if self.logging:
            self.pathFileLogging = self.def_on(
                variable=pathFileLogging,
                pathDir=pathDIR + '\logs',
                file=f'\log_{datetime.now().strftime("%d-%m-%Y %H.%M")}.log')
        
        if self.use_proxy:
            self.pathFileProxy = self.def_on(
                variable=pathFileProxy,
                pathDir=pathDIR + '\proxy',
                file='use.txt'
            )
        
        self.pathDirResult = self.def_on(
                variable=pathDirResult,
                pathDir=pathDIR + r'\result'
            )

    def def_on(self, variable:str, pathDir:str, file:Union[str, int]=None):
        if variable == 'defaut':
            if not os.path.exists(pathDir):
                os.mkdir(pathDir)
            return pathDir + file if file else pathDir
        else:
            return variable
              



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





    