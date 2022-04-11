import re
import requests



from imports import logger
from baseParser.control import ProxyPull
from baseParser.write_read import write_json

from Yarche.configure.config import Config
from Yarche.build.data_requesrt import (
    data_for_get_coordinat,
    data_for_set_adress,
    data_for_get_category,
    data_for_get_products

)
from Yarche.build.render_cvs import (
    FirstTitle, TitleCategory, TitleProduct, getCategory, getProduct)





class YarcheParserError(Exception):
    def __init__(self, message:str, itap:int):
        self.message = message
        self.itap = itap
    def __str__(self):
        return self.message


def errors(func):
    def wrapper(self, **kwargs):
        try:
            result= func(self, **kwargs)
        except YarcheParserError as error:

            try:
                logger.warning(error.message)
                self.session.proxies = next(self.proxy)
                wrapper(self, itap=error.itap)

            except StopIteration as error:
                logger.error(error)
        else:
            return result
    return wrapper








class ParseYarcheProductCategory:
    def __init__(self, config:Config, proxy:ProxyPull) -> None: 
        self.config = config
        self.proxy = proxy
        self.category_index = 0

        self._soft={
            0: {
                "func": self.build_session, 
                "message":{
                    "before": "Получение ссесии", 
                    "after": "Сессия получена: "}},
            1: {
                "func":self.get_token, 
                "message":{
                    "before": "Получение токенов для доступа к Api", 
                    "after": "Токены получены: {}"}},
            2:{
                "func": self.get_coordinats, 
                "message": {
                    "before": "Получение координат на карте по текущему адресу",
                    "after": "Координаты получены"}},
            3:{
                "func": self.set_adress,
                "message": {
                    "before": "Установка адреса в соответствии с текущими координатами",
                    "after": "Адрес установлен"}},
            4:{
                "func": self.get_categories,
                "message": {
                    "before": "Получение списка всех категорий",
                    "after": "Список категорий получен"}},
            5:{
                "func": self.get_product_category,
                "message": {
                    "before": "Получение продукта из соответствующей категории",
                    "after": "Список категорий получен"}}}
            

    @errors
    def center(self, itap:int):
        while itap <= len(self._soft.keys()):
            if self._soft.get(itap):
                logger.info(self._soft.get(itap)["message"]["before"])
                self._soft.get(itap)['func']()
                logger.info(self._soft.get(itap)['message']["after"])
            itap +=1
        else:
            next()


    def build_sesion(self):
        self.session = requests.Session
        self.session.headers = self.config.prod.headers
        self.session.proxies = next(self.proxy)
        self.session.verify = False


    def base_pages(self):
        response = self.session.get(
            url=self.config.prod.base_url)
        if response.status_code == 200:
            self.session.response = response.text
        else:
            raise YarcheParserError(message="Не получилось получить ссесию")

    
        

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
            json=data_for_get_coordinat(adress=self.config.prod.Adress[0]))
        if response.status_code == 200:
            self.coordinats = (
                response.json()["data"]["geocode"]["lat"],
                response.json()["data"]["geocode"]["long"])
        else:
            raise YarcheParserError(message="Не удалось получить координаты точки")
    
    def set_adress(self):
        response = self.session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={
                "Host": "api.magonline.ru",
                "token": self.tokens['token']},
            json=data_for_set_adress(adress=self.config.prod.Adress[0], coordinats=self.coordinats),
            verify=False)
        if response.status_code != 200 and \
            response.json()["data"]["setCurrentAddress"]["status"] != 'confirmed':
            raise YarcheParserError(message="Не удалось установить адрес")
                
            
    def get_categories(self):
        response = self.session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={
                "Host": "api.magonline.ru",
                "token": self.tokens['token']},
            json=data_for_get_category(),
            verify=False
        )
        if response.status_code == 200 and not response.json().get('errors'):
            self.before_category = response.json()['data']['categories']
        else:
            raise YarcheParserError(message="Не удалось получить категории")



    def get_product(self, category_id:int, limit:int=99, page:int=1):
        return self.session.post(
            url='https://api.magonline.ru/api/graphql',
            headers={
                    "Host": "api.magonline.ru",
                    "token": self.tokens['token']},
            json=data_for_get_products(
                category_id=category_id, 
                limit=limit,
                page=page))


    def get_product_category(self):
        for index, category in enumerate(self.before_category):
            if category.get('amount') > 0:
                products = []
                for page, amound in enumerate(
                    [99 for _ in range(category.get('amount') // 99)] + 
                    [category.get('amount') % 99], start=1):
                    response = self.get_product(
                        category_id=category.get('id'), 
                        limit=amound,
                        page=page)
                    if response.status_code == 200 and not response.json().get('errors'):
                        products.extend(response.json()['data']['products']['list'])
                    else:
                        raise YarcheParserError(message=f"Не удалось получить продукт категории '{category.get('name')}'") 
                self.before_category[index]['products'] = products
                    
           
    def result_json(self):
        write_json(
            pathFile=self.config.system.pathDirResult + fr'\result_{self.config.prod.Adress[0]}.json',
            jsonObject=self.before_category,
            indent=4)


    def result_csv(before_category):
        wb = openpyxl.Workbook()
        firstSheet = wb.create_sheet(title='Categoty', index=0)
        firstSheet.append(FirstTitle)
        index = 1
        for category in before_category:
            firstSheet.append((category.get('id'), category.get('name')))

            if category.get('products'):
                newSheet = wb.create_sheet(
                    title=category.get('name') if len(category.get('name')) < 31 else ' '.join(category.get('name').split(' ')[:-1]), 
                    index=index)

                newSheet.append(TitleCategory)
                newSheet.append(getCategory(inside=category))

                for _ in [tuple('' for _ in TitleCategory)] * 3:
                    newSheet.append(_)
                
                index += 1
                newSheet.append(TitleProduct)
                
                for product in category['products']:
                    newSheet.append(getProduct(product))

        wb.save(filename=r'C:\Users\ole lukoie\Desktop\my_parser\Yarche\result\results_Россия, Москва, Вересаева 10.xlsx')


