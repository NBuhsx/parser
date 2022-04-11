import re, more_itertools
from statistics import mode
import json
from typing import Iterable, Optional, Union




### Чтение
def read_rows(pathfile:str, mode:str='r', slice:slice=slice(0, None, 1), encoding:str='utf-8', regusl:Optional[str]=None):
    """ Возращает генератор"""
    with open(file=pathfile, mode=mode, encoding=encoding) as file:
        for row in more_itertools.islice_extended(file)[slice]:
            try: yield re.findall(regusl, row)[0] if regusl else row.strip()
            except IndexError: continue 
            

### Запись
def write_file_str(pathfile:str, write:str, mode:str='a', encoding:str='utf-8', addN:Optional[bool]=False):
    """ Записывает не итерабельный тип данных(строку) """
    with open(file=pathfile, mode=mode, encoding=encoding) as file:
        file.write(write + '\n') if addN else file.write(write)


def write_json(pathFile:str, jsonObject:Union[dict, list], ensure_ascii:bool=False, indent:int=3):
    """ Пишет Json"""
    with open(file=pathFile, mode='w', encoding='utf-8') as file:
        json.dump(obj=jsonObject, fp=file, ensure_ascii=ensure_ascii, indent=indent)

def read_json(pathfile:str, mode:str='r', encoding:str='utf-8'):
    with open(file=pathfile, mode=mode, encoding=encoding) as file:
        return json.load(fp=file)