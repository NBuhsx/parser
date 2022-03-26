import os
from fake_useragent import UserAgent
from dataclasses import dataclass, InitVar, field

from baseParser.configure.datacls import settinngSystem


@dataclass
class Parser:
   
    project_name: str = 'Ярче'
    base_url: str = 'https://yarcheplus.ru'
    headers:InitVar[bool] = False
    cookies:dict = None
    Adress:list = field(default_factory=list)


    def __post_init__(self, headers):
       self.headers = headers if headers else {"User-Agent":UserAgent().random}  
    
    




@dataclass
class SendEmail:
    login:str 
    password:str
    typeConnect:str = "smtp"
    server:str = "smtp.mail.ru"
    port:int = 465
    
   


@dataclass
class Config:
    system:settinngSystem
    prod:Parser
    

def get_config(data:dict):
    return Config(
        system=settinngSystem(
            **data['settinngSystem']
        ),
        prod=Parser(
            **data['Parser']
        ),
    )

