from email import header
from msilib.schema import Error
import re
import requests


from typing import Generator, 

class Yarche:
    parse_tokens = {
        'geotoken': '"geocoderToken":"([a-z0-9-]+)"',
        'token': '"token":"([a-z0-9-]+)"',
        'refreshToken': '"refreshToken":"([a-z0-9-]+)"'}

    def base_pages(session:requests.Session=requests, base_url:str="https://yarcheplus.ru/"):
        response =session.get(
            url=base_url,
            headers={'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27"})
        response.raise_for_status()
        return response.text

    @classmethod
    def get_tokens(cls, response:requests.Response.text) -> Generator[tuple[str, str]]:
        for tokenName, value in cls.parse_tokens.items():
            yield tokenName, re.search(pattern=value, string=response).group(0)
    
    def get_coordinats(geoToken:str, adress:str, session:requests.Session=requests):
        response = session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={'token':geoToken},
            json=data_for_get_coordinat(adress=self.config.prod.Adress[0]))



        if response.status_code == 200:
            self.coordinats = (
                response.json()["data"]["geocode"]["lat"],
                response.json()["data"]["geocode"]["long"])
        else:
            raise YarcheParserError(message="Не удалось получить координаты точки")






class Soft():
    def __init__(self, config, proxy) -> None: 
        self.config = config
        self.proxy = proxy


    def build_session(self):
        self.session = requests.Session()
        self.session.headers = self.config.prod.headers
        self.session.proxies = next(self.proxy)
        self.session.verify = False
    

    def set_token(self):
        self.tokens = Yarche.get_tokens(
            response=Yarche.base_pages(
                session=self.session,
                base_url=self.config.prod.base_url))
        for token in self.tokens:
            if not token:
                raise Error

    
    

    