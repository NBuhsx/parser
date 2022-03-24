import sys
from typing import Callable, Union



def check(func, logger:object, **kwargs):
    try:
        return func(**kwargs)
    except Exception as err:
        logger.exception(err)
        sys.exit()

class Proxy:
    def __init__(self, proxy=None) -> None:
        if proxy:
            self.proxy_pull = [self.standart_proxy(proxy=pr) for pr in proxy]
        else:
            self.proxy_pull = None

        self.proxy_pull = 0

    def get_proxy(self):
        if self.proxy_pull:
            proxy = self.proxy_pull[self.index_proxy_pool]
            self.index_proxy_pool
            return proxy
        else:
            return False
    
    def standart_proxy(self, proxy):
        return {
            'http':proxy,
            'https':proxy
        }
