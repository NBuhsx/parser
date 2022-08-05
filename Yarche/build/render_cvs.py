from typing import Callable



first_sheet_title_category = ('id', 'name',)     


def required(inside:dict, method:Callable=dict.values):
    """ Распеределение """
    match method.__name__, inside:
        case 'keys', {'image': image, 'metaTags':megaTags}:    # Заголовок категорий
            return ( 
                *(*inside,)[:6], 
                'img_id',
                'img_title',
                'metaTags_title', 
                'metaTags_value',)
        case 'keys', {'image': image, 'quant': quant}:         # Заголовок продуктов
            return ( 
                *(*inside,)[:4], 
                'img_id',
                'img_title',
                *(*inside,)[6:15],
                'currency',
                'rating',
                'numberOfRatings',)
        case 'values', {'image': image, 'metaTags':megaTags}:   # Значения для категорий
            return ( 
                *tuple(inside.values())[:6], 
                image.get('id', None),
                image.get('title', None),
                megaTags[0].get('value'),
                megaTags[1].get('value')
                )
        case 'values', {'image': image, 'quant': quant}:        # Значения для продуктов
            values = tuple(inside.values())
            return ( 
                *values[:4], 
                image.get('id', None),
                image.get('title', None),
                *values[6:16],
                quant.get('currency', "RUB"),
                inside.get('rating', None),
                inside.get('numberOfRatings', None))