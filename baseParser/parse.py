import requests

from abc import ABC, abstractclassmethod

from dataclasses import dataclass
from typing import Callable, Union



class Parse:
    def __init__(self, config:dataclass):
        self.config = config
    
    
    @staticmethod
    def get_session(url:str, headers:dict, proxy:Union[dict, None]=None):
        session = requests.Session()
        session.headers = headers
        return session.get(
            url=url,
            proxies=proxy if proxy else None
        )
        
    @staticmethod
    def check(func:Callable, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return None