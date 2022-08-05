from typing import Iterable, Union


class ProxyPull:
    def __init__(self, proxies:Union[Iterable, None]=None, noProxy:int=3) -> None:
        if proxies:
            self.proxy_pull = [
            {
                'http':proxy,
                'https':proxy} for proxy in proxies]
            self._messg_error = 'Список прокси исчерпан' 
        else:
            self.proxy_pull = [None for _ in range(noProxy)]
            self._messg_error = 'Количестов попыток исчерпано'
        self._index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            self._index += 1
            return self.proxy_pull[self._index]
        except IndexError:
            raise StopIteration(self._messg_error)



