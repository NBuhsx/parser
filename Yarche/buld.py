import re

from baseParser.parse import get_session
from baseParser.control import Proxy
from Yarche.configure.config import Config


class ParseYarche:
    def __init__(self, config:Config, proxy:Proxy) -> None:
        self.config = config
        self.proxy = proxy

    def CENTER(self):
        self.session = get_session(
            url=self.config.prod.base_url,
            headers=self.config.prod.headers,
            proxy=self.proxy.get_proxy())
        
        self.session.headers['token'] = self.get_token()
       



    
    def get_token(self):
        return re.findall(
            pattern='"token":"(\w+\-\w+)",',
            string=self.session.response)[0]
    
