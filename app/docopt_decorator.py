import sys
import cmd
from docopt import docopt, DocoptExit

"""
	This class shall be used as a decorator to easily parse commandline arguments to the main cmd loop

"""
def DocoptInteractive(func):
	"""
	This decorator is used to simplify the try/except block and pass the result
	of the docopt parsing to the called action.
	"""

	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)

		except DocoptExit as e:
			# The DocoptExit is thrown when the args do not match.
			# We print a message to the user and the usage block.

			print('Invalid Command!')
			print(e)
			return

		except SystemExit:
			# The SystemExit exception prints the usage for --help
			# We do not need to do the print here.

			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn