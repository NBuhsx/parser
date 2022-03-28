import re
import openpyxl


from baseParser.parse import get_session
from baseParser.control import ProxyPull
from Yarche.configure.config import Config

from Yarche.data_requesrt import (
    data_for_get_coordinat,
    data_for_set_adress,
    data_for_get_category,
    data_for_get_products

)


class ParseError(Exception):
    pass

class ParseYarcheProductCategory:
    def __init__(self, config:Config, proxy:ProxyPull) -> None:
        self.config = config
        self.proxy = proxy


        self._soft={
            0: self.build_session,
            1: self.get_token,
            2: self.get_coordinats,
            3: self.set_adress,
            4: self.parse_product_category
        }
    
    def __call__(self, itap:int):
        while itap < len(self._soft.keys()):
            if self._soft.get(itap):
                self._soft[itap]()
            itap +=1 

        

        # self.build_session()
        # self.get_token()
        # self.get_coordinats()
        # self.set_adress()
        # self.check_category()
        # self.parse_product_category()
        # self.write()



    def build_session(self):
        self.session = get_session(
            url=self.config.prod.base_url,
            headers=self.config.prod.headers,
            proxy=self.proxy.getProxy()
        )

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


    def get_coordinats(self):
        response = self.session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={'token':self.tokens['geotoken']},
            json=data_for_get_coordinat(adress=self.config.prod.Adress[0]),
            verify=False)
        if response.status_code == 200:
            self.coordinats = (
                response.json()["data"]["geocode"]["lat"],
                response.json()["data"]["geocode"]["long"])
            
        else:
            raise "Произошла ошибка при поиске координат"
    
    def set_adress(self):
        response = self.session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={
                "Host": "api.magonline.ru",
                "token": self.tokens['token']},
            json=data_for_set_adress(adress=self.config.prod.Adress[0], coordinats=self.coordinats),
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
                break
           
    
    def errors(self):
        self.er = {
            'error': ParseError, 'func':(self.CENTER), 'kwargs':({'itap':-1}),
            'error': ConnectionError, 'func':(self.proxy.getProxy, self.CENTER), 'kwargs':({'itap':-1})
    }


    def write(self):
        wb = openpyxl.Workbook()
        for index, catagory in enumerate(self.before_category):
            ws = wb.create_sheet(title=catagory['name'], index=index)
            for cat in [tuple(catagory.values())[:-1], tuple(catagory.keys())[:-1]]:
                ws.append(str(cat))
                ws.insert_rows(3, 2)
            for product in [tuple(catagory['products'].values()), tuple(catagory['products'].keys())]:
                ws.append(str(product))

        wb.save("table.xlsx")   
       