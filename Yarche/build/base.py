import re
import requests



from typing import Dict, Generator, Tuple, Any



# from build.data_requesrt import (
#     data_for_get_coordinat,
#     data_for_set_adress,
#     data_for_get_category,
#     data_for_get_products

# )




class YarcheBase:
    parse_tokens = {
        'geotoken': '"geocoderToken":"([a-z0-9-]+)"',
        'token': '"token":"([a-z0-9-]+)"',
        'refreshToken': '"refreshToken":"([a-z0-9-]+)"'}

    @staticmethod
    def response_base_url(session:requests | requests.Session=requests) -> str:
        response = session.get(url="https://yarcheplus.ru")
        response.raise_for_status()
        return response.text
    
    @classmethod
    def get_tokens(cls, response:str) -> Generator[Tuple[str, str], None, None]:
        for tokenName, value in cls.parse_tokens.items():
            if search := re.search(pattern=value, string=response):
                yield tokenName, search.group(1)

    @staticmethod
    def get_coordinats(geo_token:str, adress:str, 
            session:requests | requests.Session=requests) -> Tuple[int, int]:
        response = session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={'token':geo_token},
            json=data_for_get_coordinat(adress=adress))
        response.raise_for_status()
        return (
                response.json()["data"]["geocode"].get("lat"),
                response.json()["data"]["geocode"].get("long"))

    @staticmethod
    def set_adress(verif_token:str, adress:str, coordinats:Tuple[str|int, str|int], 
            session:requests | requests.Session=requests) -> Dict[str, Any]:
        response = session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={
                "Host": "api.magonline.ru",
                "token": verif_token},
            json=data_for_set_adress(adress=adress, coordinats=coordinats))
        response.raise_for_status()
        return response.json()
    
    @staticmethod
    def get_categories(verif_token:str, session:requests | requests.Session=requests) -> Dict[str, Any]:
        response = session.post(
            url='https://geocoder.magonline.ru/api/graphql',
            headers={
                "Host": "api.magonline.ru",
                "token": verif_token},
            json=data_for_get_category())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_product(verif_token:str, category_id:int | str, 
                    limit:int | str=99, page:int | str=1, 
                    session:requests | requests.Session=requests) -> Dict[str, Any]:
        response = session.post(
            url='https://api.magonline.ru/api/graphql',
            headers={
                    "Host": "api.magonline.ru",
                    "token": verif_token},
            json=data_for_get_products(
                category_id=category_id, 
                limit=limit,
                page=page))
        response.raise_for_status()
        return response.json()



