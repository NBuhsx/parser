from loguru import logger
import os.path, sys


def _():
    sys.path.append(
         os.path.dirname(
            p = os.path.dirname(
                p=os.path.realpath(__file__))
    ))


_()

from baseParser.logger.app_loggers import BaseConf

logger.configure(**config)