from pydantic import BaseModel, Field, FilePath, DirectoryPath, parse_raw_as
from pydantic.tools import parse_file_as, parse_obj_as




class settinngSystem(BaseModel):
    use_thread: bool = Field(
        default=False,
        description="Use thread")
    thread: int = Field(
        default=1,
        description='Count thread',
        le=100,
        ge=1)
    use_proxy: bool = Field(
        default=False,
        description="Use proxies")
    path_file_proxy:FilePath = Field(
        default='/proxy/proxies.txt',
        description="Path proxy file")
    logging: bool = Field(
        default=True,
        description="Logging")
    path_dir_logging: DirectoryPath = Field(
        default='Yarche/logs',
        description="Logging dir")
    path_dir_result: DirectoryPath = Field(
        default='Yarche/result',
        description="Result dir")
    result_mode: str = Field(
        default='JSON',
        description='result mode json | cvs'
    )
    
    class Config:
        extra: str = 'forbid' 



class Parser(BaseModel):
    project_name: str = 'Ярче'
    headers: dict = Field(
        default={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27"},
        description="headers on session")
    parse_adress: list = Field(
        default=["Россия, Москва, Петровка 1"],
        description="shipping or store address")



class Config(BaseModel):
    setting_system: settinngSystem
    parser: Parser




# import os, sys

# from dataclasses import dataclass, InitVar, field
# from datetime import datetime
# from typing import Union



# path_dir = os.path.abspath(os.path.dirname(sys.argv[0]))



# @dataclass
# class settinngSystem:
#     use_thread:bool = False
#     thread:int = 10
#     use_proxy:bool = False
#     pathFileProxy:InitVar[str] = 'defaut'
#     logging:bool = True 
#     pathFileLogging:InitVar[str] = 'defaut'
#     pathDirResult:InitVar[str] = 'defaut'

#     def __post_init__(self, 
#             pathFileProxy:Union[str, bool], 
#             pathFileLogging:Union[str, bool],
#             pathDirResult:Union[str, bool]):

#         pathDIR = os.path.abspath(os.path.dirname(sys.argv[0]))

#         if self.logging:
#             self.pathFileLogging = self.def_on(
#                 variable=pathFileLogging,
#                 pathDir=pathDIR + '/logs',
#                 file=f'/log_{datetime.now().strftime("%d-%m-%Y %H.%M")}.log')
        
#         if self.use_proxy:
#             self.pathFileProxy = self.def_on(
#                 variable=pathFileProxy,
#                 pathDir=pathDIR + '/proxy',
#                 file='/use.txt'
#             )
        
#         self.pathDirResult = self.def_on(
#                 variable=pathDirResult,
#                 pathDir=pathDIR + '/result'
#             )

#     def def_on(self, variable:str, pathDir:str, file:Union[str, int]=None):
#         if variable == 'defaut':
#             if not os.path.exists(pathDir):
#                 os.mkdir(pathDir)
#             return pathDir + file if file else pathDir
#         else:
#             return variable
              



# @dataclass
# class SendEmail:
#     typeConnect:str
#     server:str
#     port:int
#     login:str
#     password:str



# @dataclass
# class Config:
#     base_url:str



# import json


# def parse_config(pathfile:str):
#     with open(file=pathfile, mode='r', encoding='utf-8') as file:
#         return json.load(file)

# def write_config(pathfile:str, text:dict, mode:str='w'):
#     with open(file=pathfile, mode=mode, encoding='utf-8') as file:
#         json.dump(text, file, indent=4, ensure_ascii=False)

# @dataclass
# class Parser:
   
#     project_name: str = 'Ярче'
#     base_url: str = 'https://yarcheplus.ru'
#     headers:InitVar[dict] = {}
#     cookies:dict = None
#     adress:list = field(default_factory=list)


#     def __post_init__(self, headers):
#        self.headers = headers if headers else {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27"}  
    
    




# @dataclass
# class SendEmail:
#     login:str 
#     password:str
#     typeConnect:str = "smtp"
#     server:str = "smtp.mail.ru"
#     port:int = 465
    
   


# @dataclass
# class Config:
#     system:settinngSystem
#     prod:Parser
    

# def get_config(data:dict):
#     return Config(
#         system=settinngSystem(
#             **data['settinngSystem']
#         ),
#         prod=Parser(
#             **data['Parser']
#         ),
#     )

