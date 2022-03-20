import os
from dataclasses import dataclass
from datetime import datetime





@dataclass
class settinngSystem:
    use_thread:bool = False
    thread:int = 10
    use_proxy:bool = False
    pathFileProxy:str = os.path.dirname(__file__) + r'\proxy\Use.txt'
    logging: bool = True
    pathFileLogging:str = os.path.dirname(__file__) + f'\logging\log_{datetime.now().strftime("%d-%m-%Y %H:%M")}.txt'


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




