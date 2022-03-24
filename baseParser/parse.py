import sys
from weakref import proxy
import requests

from abc import ABC, abstractclassmethod

from dataclasses import dataclass
from typing import Callable, Iterable, Union



def get_session(url:str, headers:dict, proxy:Union[dict, None]=None):
    print(proxy)
    session = requests.Session()
    session.headers = headers
    response = session.get(
            url=url,
            proxies=proxy)
    if response.status_code == 200:
        session.response = response.text
        return session
