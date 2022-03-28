import sys
from typing import Callable, Iterable, Union



def check(func, logger:object, **kwargs):
    try:
        return func(**kwargs)
    except Exception as err:
        logger.exception(err)
        sys.exit()


class ProxyPull:
    def __init__(self, proxies:Union[Iterable, None]=None, noProxy:int=3) -> None:
        if proxies:
            self.proxy_pull = [
            {
                'http':proxy,
                'https':proxy} for proxy in proxies]
        else:
            self.proxy_pull = [None for _ in range(noProxy)]
        self.count_proxy = len(self.proxy_pull)
        self.index = 0

    def getProxy(self):
        return self.proxy_pull[self.index]
    
    def change(self):
        self.index += 1