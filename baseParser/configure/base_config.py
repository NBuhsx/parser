import json




def parse_config(pathfile:str):
    with open(file=pathfile, mode='r', encoding='utf-8') as file:
        return json.load(file)

def write_config(pathfile:str, text:dict, mode:str='w'):
    with open(file=pathfile, mode=mode, encoding='utf-8') as file:
        json.dump(text, file, indent=4, ensure_ascii=False)


