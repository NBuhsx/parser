import re


from baseParser.parse import get_session
from baseParser.control import ProxyPull
from Yarche.configure.config import Config

from Yarche.data_requesrt import (
    data_for_get_coordinat,
    data_for_set_adress,
    data_for_get_category,
    data_for_get_products

)


class ParseYarcheProductCategory:
    def __init__(self, config:Config, proxy:ProxyPull) -> None:
        self.config = config
        self.proxy = proxy


    def CENTER(self):
        self.session = get_session(
            url=self.config.prod.base_url,
            headers=self.config.prod.headers,
            proxy=self.proxy.getProxy()
        )


        self.get_token()
        self.get_coordinats(adress=self.config.prod.Adress[0])
        self.set_adress(adress=self.config.prod.Adress[0])
        self.check_category()
        self.parse_product_category()


    def get_token(self):
        self.tokens = {
            'geotoken': re.findall(
                    pattern='"geocoderToken":"([a-z0-9-]+)"',
                    string=self.session.response)[0],
            'token': re.findall(
                    pattern='"token":"([a-z0-9-]+)"',
                    string=self.session.response)[0],
            'refreshToken':re.findall(
                    pattern='"refreshToken":"([a-z0-9-]+)"',
                    string=self.session.response)[0]
        }


    def get_coordinats(self, adress:str):
        response = self.session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={'token':self.tokens['geotoken']},
            json=data_for_get_coordinat(adress=adress),
            verify=False)
        if response.status_code == 200:
            self.coordinats = (
                response.json()["data"]["geocode"]["lat"],
                response.json()["data"]["geocode"]["long"])
            
        else:
            raise "Произошла ошибка при поиске координат"
    
    def set_adress(self, adress:str):
        response = self.session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={
                "Host": "api.magonline.ru",
                "token": self.tokens['token']},
            json=data_for_set_adress(adress=adress, coordinats=self.coordinats),
            verify=False)
        print(response.text)
        if response.status_code == 200:
            if response.json()["data"]["setCurrentAddress"]["status"] == 'confirmed':
                return True
        else:
            raise "Произошла ошибка при установке адреса"


    def check_category(self):
        response = self.session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={
                "Host": "api.magonline.ru",
                "token": self.tokens['token']},
            json=data_for_get_category(),
            verify=False
        )
        if response.status_code == 200:
            self.before_category = response.json()['data']['categories']

    def parse_product_category(self):
        for index, category in enumerate(self.before_category):
            response = self.session.post(
                url='https://api.magonline.ru/api/graphql',
                headers={
                    "Host": "api.magonline.ru",
                    "token": self.tokens['token']},
                json=data_for_get_products(category_id=category['id'], limit=category['amount']),
                verify=False)
            if response.status_code == 200:
                self.before_category[index]['products'] = response.json()['data']['products']['list']
           
               