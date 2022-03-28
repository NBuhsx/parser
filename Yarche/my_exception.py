
from ast import arg
from webbrowser import get


class ParseError(Exception):
    pass

class B(Exception):
    def __init__(self, parse):

        self.parse = parse
        # if hasattr(parse, 'errors'):
    def errors(self):
        s = {'error': ParseError, 'action':[
            self.parse.Center(-1)
            ]}

        

class MyCustomError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None
    

    def __str__(self) -> str:
        if self.message:
            return f"MyCustomError, {self.message}"
        else:
            return "MyCistomError has been raise"



class Power(object):
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, *param_arg):
		if len(param_arg) == 1:
			def wrapper(a, b):
				retval = param_arg[0](a, b)
				return retval ** self._arg
			return wrapper
		else:
			expo = 2
			retval = self._arg(param_arg[0], param_arg[1])
			return retval ** expo


# @Power(3)
# def multiply_together(a, b):
# 	return a * b


@Power
def multiply_together(a, b):
	return a * b


print(multiply_together(2, 2))