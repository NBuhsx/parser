import sys
from typing import Dict, Any
from loguru import logger


my_config:Dict[str, Any] = {
    "handlers": [
        {
            "sink": sys.stdout, 
            "colorize":True, 
            "format": "<y>{time:HH:mm:ss.SSS}</y> | "
                      "<level>{level: <8}</level> | "
                      "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> |"
                      "<y>{elapsed}</y>"
        },
    ],
    "extra": {"user": "someone"}
}


logger.configure(**my_config)









# def get_tlg_handler(conf: dict, loggin_level=logging.WARNING):
#     formatter = logging.Formatter('<b>%(name)s:%(levelname)s</b> - <code>%(message)s</code>')
#     tg_handler = TgLoggerHandler(
#         token=conf['tlgrm']['token'],
#         user_id=conf['tlgrm']['reciever_id']
#     )
#     tg_handler.setLevel(level=loggin_level)
#     tg_handler.setFormatter(formatter)
#     return tg_handler


# class TgLoggerHandler(logging.StreamHandler):
#     def init(self, token, user_id):
#         super().init()
#         self.user_id = user_id
#         self.token = token

#     def emit(self, record):
#         try:
#             requests.post('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(
#                 self.token, self.user_id, record))
#         except Exception as e:
#             logging.exception("Ошибка при отправке сообщения в телеграмм: \n {0}".format(e))