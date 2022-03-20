import os.path, sys


def _():
    sys.path.append(
         os.path.dirname(
            p = os.path.dirname(
                p=os.path.realpath(__file__))
    ))


_()